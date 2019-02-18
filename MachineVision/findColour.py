import cv2
import numpy as np


def findColour(filename, colour) -> object:
    """Function that takes path of an image and outputs a new file highlighting said colour.
    :param filename: name of image you want to process
    :param colour: the colour you want to extract (green/red)
    """

    image = cv2.imread(filename, 1)  # gcolour
    blurred_image = cv2.GaussianBlur(image, (5, 5), 0)  # blurred to remove noise
    hsv = cv2.cvtColor(blurred_image, cv2.COLOR_BGR2HSV)

    # RED COLOUR BOUNDARIES
    red_lower = np.array([0, 150, 0])  # pair of least red and most red on the hsv map
    red_upper = np.array([7, 255, 359])
    wrap_around_lower = np.array([170, 150, 0])    # still need tweaking, doesnt pick up very light reds
    wrap_around_upper = np.array([180, 255, 359])  # Could draw box around item to remedy this?

    # GREEN COLOUR BOUNDARIES
    green_lower = np.array([40, 60, 60])
    green_upper = np.array([80, 359, 359])

    if colour == "red":
        mask = cv2.inRange(hsv, red_lower, red_upper)
        additional_mask = cv2.inRange(hsv, wrap_around_lower, wrap_around_upper)
        mask += additional_mask
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL,  # finds the edges between white and black for the mask
                                       cv2.CHAIN_APPROX_SIMPLE)  # contours returns an array with every edge AFAIK
        contoured = cv2.drawContours(image, contours, -1, (255, 0, 0), 3)  # draws the edges
        cv2.imwrite('./Output/' + colour + '1.jpg', contoured)

    if colour == "green":
        mask = cv2.inRange(hsv, green_lower, green_upper)
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL,
                                       cv2.CHAIN_APPROX_SIMPLE)
        contoured = cv2.drawContours(image, contours, -1, (255, 0, 0), 3)
        cv2.imwrite('./Output/' + colour + '1.jpg', contoured)

    output = cv2.bitwise_and(image, image, mask=mask)  # highlights our mask onto the original image
    cv2.imwrite('./Output/' + colour + '2.jpg', output)

    if len(contours) != 0:  # check if there's anything in contours
        cv2.drawContours(output, contours, -1, 255, 3)  # draws contours in blue

        c = max(contours, key=cv2.contourArea)  # finds contour with largest area

        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(output, (x, y), (x + w, y + h), (0, 255, 0), 2)  # draw rectangle around largest cone
        cv2.imwrite('./Output/' + colour + 'LargestArea.jpg', output)

    for contour in contours:
        area = cv2.contourArea(
            contour)  # returns the area of contour (i dont know what unit it returns it as (possibly pixels?))

        if area > 5000:  # draw the edges in green if the area is > 5000
            cnt_area = cv2.drawContours(image, contour, -1, (0, 255, 0), 3)
            cv2.imwrite('./Output/' + colour + 'cntArea.jpg', cnt_area)


if __name__ == "__main__":
    findColour("./Assets/test3.jpg", "red")
