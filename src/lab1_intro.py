# src/lab1_intro.py
import cv2
import numpy as np
from matplotlib import pyplot as plt
from pathlib import Path
# import easygui

# --- paths (relative to repo root) ---
ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "samples"
OUT  = ROOT / "output"
OUT.mkdir(parents=True, exist_ok=True)


# 1) Test on a default sample first
default_img = DATA / "Mountains_Scotland.jpg" 
img_path = "data/samples/Mountains_Scotland.jpg"

# 2) If default missing - through the GUI
# if not img_path.exists():
#     chosen = easygui.fileopenbox(title="Choose an image",
#                                  default=str(ROOT / "**" / "*.jpg"))
#     if chosen:
#         img_path = Path(chosen)
#     else:
#         raise FileNotFoundError(
#             f"No image selected and default not found: {default_img}"
#         )

# print(f"[INFO] Loading: {img_path}")

# --- read image (BGR) ---
I = cv2.imread(str(img_path))
if I is None:
    raise FileNotFoundError(f"Failed to read image at: {img_path}")

# --- show with OpenCV (BGR) ---
try:
    cv2.imshow("Original (BGR)", I)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
except Exception as e:
    print(f"[WARN] cv2.imshow failed ({e}). Using matplotlib instead.")

# --- save original copy ---
cv2.imwrite(str(OUT / "capture_test.jpg"), I)

# --- matplotlib display (needs RGB) ---
RGB = cv2.cvtColor(I, cv2.COLOR_BGR2RGB)
plt.imshow(RGB)
plt.title("Original in RGB (Matplotlib)")
plt.axis("off")
plt.show()

# --- color space conversions ---
HSV = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)
YUV = cv2.cvtColor(I, cv2.COLOR_BGR2YUV)
GRAY = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)

# --- access pixels ---
B = I[50, 100, 0]
G = I[50, 100, 1]
R = I[50, 100, 2]
BGR = I[50, 100]
print(f"[PIXEL] (50,100) BGR={BGR} (B={B}, G={G}, R={R})")

# --- modify pixels/region (blue patch) ---
I_mod = I.copy()
I_mod[50, 100] = (255, 0, 0)
I_mod[100:200, 300:400] = (255, 0, 0)
cv2.imwrite(str(OUT / "modified_patch.jpg"), I_mod)

print(f"[OK] Wrote: {OUT/'capture_test.jpg'} and {OUT/'modified_patch.jpg'}")
