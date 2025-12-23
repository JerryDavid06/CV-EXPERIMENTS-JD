import cv2
import numpy as np

# ---------- Load video ----------
cap = cv2.VideoCapture(
    r"C:\Users\Jerry David\OneDrive\Desktop\CV EX\video.mp4"
)

if not cap.isOpened():
    print("Error: Cannot open video")
    exit()

# Read first frame to get dimensions
ret, frame = cap.read()
if not ret:
    print("Error: Cannot read frame")
    exit()

h, w = frame.shape[:2]

# ---------- Define source points ----------
pts1 = np.float32([
    [50, 50],        # top-left
    [w - 50, 50],    # top-right
    [50, h - 50],    # bottom-left
    [w - 50, h - 50] # bottom-right
])

# ---------- Define destination points ----------
pts2 = np.float32([
    [100, 100],
    [w - 150, 80],
    [150, h - 100],
    [w - 100, h - 50]
])

# Perspective matrix
perspective_matrix = cv2.getPerspectiveTransform(pts1, pts2)

# Reset video to first frame
cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

# ---------- Process video ----------
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Apply perspective transformation
    transformed = cv2.warpPerspective(frame, perspective_matrix, (w, h))

    # Display results
    cv2.imshow("Original Video", frame)
    cv2.imshow("Perspective Transformed Video", transformed)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
