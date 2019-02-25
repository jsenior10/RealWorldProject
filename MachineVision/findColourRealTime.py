import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    blurred_frame = cv2.GaussianBlur(frame, (5,5), 0)
    hsv = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)

    red_lower = np.array([0, 150, 0])  # pair of least red and most red on the hsv map
    red_upper = np.array([7, 255, 359])
    wrap_around_lower = np.array([170, 150, 0])  # still need tweaking, doesnt pick up very light reds
    wrap_around_upper = np.array([180, 255, 359])
    mask = cv2.inRange(hsv, red_lower, red_upper)
    add_mask= cv2.inRange(hsv, wrap_around_lower,wrap_around_upper)
    mask += add_mask
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    for contour in contours:
        area = cv2.contourArea(contour)

        if area > 500:
            cv2.drawContours(frame, contour, -1, (0,255,0), 3)

    if len(contours) != 0:  # check if there's anything in contours
        cv2.drawContours(frame, contours, -1, 255, 3)  # draws contours in blue

        c = max(contours, key=cv2.contourArea)  # finds contour with largest area

        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # draw rectangle around largest cone

    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
