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

# ---------- Boundary Detection Kernel ----------
boundary_kernel = np.array([
    [-1, -1, -1],
    [-1,  8, -1],
    [-1, -1, -1]
], dtype=np.float32)

# Apply convolution
boundary = cv2.filter2D(gray, cv2.CV_64F, boundary_kernel)

# Convert to displayable format
boundary_abs = cv2.convertScaleAbs(boundary)

# ---------- Display Results ----------
cv2.imshow("Original Grayscale Image", gray)
cv2.imshow("Boundary Detected Image", boundary_abs)

cv2.waitKey(0)
cv2.destroyAllWindows()
