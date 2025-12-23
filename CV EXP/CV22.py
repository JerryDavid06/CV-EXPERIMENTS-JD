import cv2
import numpy as np

# ---------- Unicode-safe image loading ----------
image_path = r"C:\Users\Jerry David\OneDrive\문서\CV EXP\test.jpg"

with open(image_path, "rb") as f:
    data = np.frombuffer(f.read(), np.uint8)

img = cv2.imdecode(data, cv2.IMREAD_COLOR)

# Safety check
if img is None:
    print("Error: Image not loaded")
    exit()

# ---------- Watermark Text ----------
watermark_text = "JERIDS"

# Get image dimensions
h, w = img.shape[:2]

# Position of watermark (bottom-right corner)
position = (w - 300, h - 30)

# Font settings
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 0.8
color = (255, 255, 255)   # White color
thickness = 2

# ---------- Insert Watermark ----------
watermarked_image = img.copy()
cv2.putText(
    watermarked_image,
    watermark_text,
    position,
    font,
    font_scale,
    color,
    thickness,
    cv2.LINE_AA
)

# ---------- Display Results ----------
cv2.imshow("Original Image", img)
cv2.imshow("Watermarked Image", watermarked_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
