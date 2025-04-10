import cv2
import numpy as np
import time

# === CONFIGURATION ===
cloak_color = "red" 

# === INITIALIZATION ===
cap = cv2.VideoCapture(0)
time.sleep(2)

# === CAPTURE BACKGROUND ===
print("Capturing background...")
for i in range(60):
    ret, background = cap.read()
    if ret:
        background = np.flip(background, axis=1)

# === MASK FILTER FUNCTION ===
def filter_mask(mask):
    open_kernel = np.ones((5, 5), np.uint8)
    close_kernel = np.ones((7, 7), np.uint8)
    dilation_kernel = np.ones((10, 10), np.uint8)

    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, close_kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, open_kernel)
    mask = cv2.dilate(mask, dilation_kernel, iterations=1)
    return mask

# === MAIN LOOP ===
print("Cloak effect started. Press ESC to exit.")
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = np.flip(frame, axis=1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    if cloak_color == "red":
        lower1 = np.array([0, 120, 70])
        upper1 = np.array([10, 255, 255])
        lower2 = np.array([170, 120, 70])
        upper2 = np.array([180, 255, 255])

        mask1 = cv2.inRange(hsv, lower1, upper1)
        mask2 = cv2.inRange(hsv, lower2, upper2)
        mask = mask1 + mask2

    elif cloak_color == "green":
        lower = np.array([50, 80, 50])
        upper = np.array([90, 255, 255])
        mask = cv2.inRange(hsv, lower, upper)

    else:
        raise ValueError("Unsupported cloak color: Choose 'red' or 'green'")

    # Filter the mask
    mask = filter_mask(mask)

    # Create the final output
    cloak_area = cv2.bitwise_and(background, background, mask=mask)
    inverse_mask = cv2.bitwise_not(mask)
    non_cloak_area = cv2.bitwise_and(frame, frame, mask=inverse_mask)

    final_output = cv2.add(cloak_area, non_cloak_area)

    cv2.imshow("Invisibility Cloak", final_output)

    key = cv2.waitKey(1)
    if key == 27:  # ESC key to exit
        break

# === CLEANUP ===
cap.release()
cv2.destroyAllWindows()