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

# ---------- Step 1: Blur the image ----------
blurred = cv2.GaussianBlur(gray, (5, 5), 1.0)

# ---------- Step 2: Create Unsharp Mask ----------
unsharp_mask = cv2.subtract(gray, blurred)

# ---------- Step 3: Add mask to original ----------
# k controls sharpening strength (1.0 is standard)
sharpened = cv2.add(gray, unsharp_mask)

# ---------- Display Results ----------
cv2.imshow("Original Grayscale Image", gray)
cv2.imshow("Blurred Image", blurred)
cv2.imshow("Unsharp Mask", unsharp_mask)
cv2.imshow("Sharpened Image (Unsharp Masking)", sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()
