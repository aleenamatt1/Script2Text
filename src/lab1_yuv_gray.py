# src/lab1_yuv_gray.py
import cv2
import matplotlib.pyplot as plt
from pathlib import Path

# --- paths ---
ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "samples"
OUT  = ROOT / "output"
OUT.mkdir(parents=True, exist_ok=True)

# --- load image ---
img_path = DATA / "Mountains_Scotland.jpg"  # change to your sample
I = cv2.imread(str(img_path))
if I is None:
    raise FileNotFoundError(f"Image not found: {img_path}")

# --- convert to YUV and extract Y channel ---
YUV = cv2.cvtColor(I, cv2.COLOR_BGR2YUV)
Y_channel = YUV[:, :, 0]

# --- convert to grayscale (intensity) ---
GRAY = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)

# --- show with OpenCV ---
cv2.imshow("Y Channel (Luminance)", Y_channel)
cv2.imshow("Grayscale (Intensity)", GRAY)
cv2.waitKey(0)
cv2.destroyAllWindows()

# --- show side by side with Matplotlib ---
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title("Y Channel (Luminance)")
plt.imshow(Y_channel, cmap="gray")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.title("Grayscale (Intensity)")
plt.imshow(GRAY, cmap="gray")
plt.axis("off")

plt.tight_layout()
plt.savefig(OUT / "yuv_vs_gray.png", dpi=200)
plt.show()

cv2.imwrite(str(OUT / "y_channel.png"), Y_channel)
cv2.imwrite(str(OUT / "grayscale.png"), GRAY)
plt.savefig(OUT / "yuv_vs_gray.png", dpi=200)

print(f"[OK] Saved comparison figure to: {OUT/'yuv_vs_gray.png'}")
