import numpy as np
import cv2
from pathlib import Path

# ensure output dir exists
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output"
OUT.mkdir(parents=True, exist_ok=True)

print("OpenCV version:", cv2.__version__)

# Create a blank white image and put text on it
img = 255 * np.ones((200, 500, 3), dtype="uint8")
cv2.putText(img, "Script2Text Project", (20, 110),
            cv2.FONT_HERSHEY_SIMPLEX, 1.1, (0, 0, 0), 2, cv2.LINE_AA)

out_path = OUT / "hello_opencv.png"
cv2.imwrite(str(out_path), img)
print(f"[OK] Created: {out_path}")
