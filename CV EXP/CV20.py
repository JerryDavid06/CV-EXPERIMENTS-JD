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

# ---------- Convert to Grayscale ----------
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# ---------- High-Boost Mask ----------
A = 2  # A >= 1 (increase A for stronger sharpening)

high_boost_kernel = np.array([
    [0, -1,  0],
    [-1, A + 4, -1],
    [0, -1,  0]
], dtype=np.float32)

# Apply High-Boost filtering
high_boost = cv2.filter2D(gray, cv2.CV_64F, high_boost_kernel)

# Convert to displayable format
high_boost_abs = cv2.convertScaleAbs(high_boost)

# ---------- Display Results ----------
cv2.imshow("Original Grayscale Image", gray)
cv2.imshow("High-Boost Sharpened Image", high_boost_abs)

cv2.waitKey(0)
cv2.destroyAllWindows()
