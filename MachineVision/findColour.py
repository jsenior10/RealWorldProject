import cv2
import numpy as np


def findColour(filename, colour):
    """Function that takes path of an image and outputs a new file highlighting said colour."""

    image = cv2.imread(filename, 1)  # gcolour
    blurred_image = cv2.GaussianBlur(image, (5, 5), 0)  # blurred to remove noise
    hsv = cv2.cvtColor(blurred_image, cv2.COLOR_BGR2HSV)

    red_lower = np.array([0, 150, 0])  # pair of least red and most red on the hsv map
    red_upper = np.array([7, 255, 359])
    wrap_around_lower = np.array([170, 150, 0])  # still need tweaking, doesnt pick up very light reds
    wrap_around_upper = np.array([180, 255, 359])

    mask = cv2.inRange(hsv, red_lower, red_upper)
    if colour == "red":
        additional_mask = cv2.inRange(hsv, wrap_around_lower, wrap_around_upper)
        mask += additional_mask
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL,
                                       cv2.CHAIN_APPROX_NONE)  # finds the edges between white and black for the mask
        contoured = cv2.drawContours(image, contours, -1, (255, 0, 0), 3)  # draws the edges
        cv2.imwrite('output1.jpg', contoured)

    output = cv2.bitwise_and(image, image, mask=mask)  # highlights our mask onto the original image

    cv2.imwrite('output2.jpg', output)

    for contour in contours:
        area = cv2.contourArea(
            contour)  # returns the area of contour (i dont know what unit it returns it as (possibly pixels?))

        if area > 5000:  # draw the edges in green if the area is > 5000
            cnt_area = cv2.drawContours(image, contour, -1, (0, 255, 0), 3)
            cv2.imwrite('cntArea.jpg', cnt_area)


if __name__ == "__main__":
    findColour("/home/codio/workspace/WheelieVehicle/Assets/hsvMap.jpg", "red")
