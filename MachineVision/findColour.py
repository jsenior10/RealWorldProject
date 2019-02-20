import cv2
import numpy as np


def findColour(openCVobject, output = False) -> object:
    """Function that takes path of an image and outputs a new file highlighting said colour.
    :param openCVobject: variable pointing to an openCVobject 
    :param output: whether you want it saved to the file system as well or not 
    """

    image = openCVobject  # gcolour
    blurred_image = cv2.GaussianBlur(image, (5, 5), 0)  # blurred to remove noise
    hsv = cv2.cvtColor(blurred_image, cv2.COLOR_BGR2HSV)

    # RED COLOUR BOUNDARIES
    red_lower = np.array([0, 150, 60])  # pair of least red and most red on the hsv map
    red_upper = np.array([7, 255, 359])
    wrap_around_lower = np.array([170, 150, 60])  # still need tweaking, doesnt pick up very light reds
    wrap_around_upper = np.array([180, 255, 359])  # Could draw box around item to remedy this?

    # GREEN COLOUR BOUNDARIES
    green_lower = np.array([40, 60, 60])
    green_upper = np.array([80, 359, 359])
    
    #red detection
    maskRed = cv2.inRange(hsv, red_lower, red_upper)
    additional_mask = cv2.inRange(hsv, wrap_around_lower, wrap_around_upper)
    maskRed += additional_mask

    #green detection 
    maskGreen = cv2.inRange(hsv, green_lower, green_upper)

    if output:
        contoursRed, _ = cv2.findContours(maskRed, cv2.RETR_EXTERNAL,  # finds the edges between white and black for the mask
                                       cv2.CHAIN_APPROX_SIMPLE)  # contours returns an array with every edge AFAIK
        contouredRed = cv2.drawContours(image, contoursRed, -1, (255, 0, 0), 3)  # draws the edges
        cv2.imwrite('./Output/red1.jpg', contouredRed)
        
        contoursGreen, _ = cv2.findContours(maskGreen, cv2.RETR_EXTERNAL,
                                       cv2.CHAIN_APPROX_SIMPLE)
        contouredGreen = cv2.drawContours(image, contoursGreen, -1, (255, 0, 0), 3)
        cv2.imwrite('./Output/green1.jpg', contouredGreen)
        
        outputImage1 = cv2.bitwise_and(image, image, mask=maskRed)  # highlights our mask onto the original image
        cv2.imwrite('./Output/red2.jpg', outputImage1)
        
        outputImage2 = cv2.bitwise_and(image, image, mask=maskGreen)  # highlights our mask onto the original image
        cv2.imwrite('./Output/green2.jpg', outputImage2)
    
    return maskRed, maskGreen 
"""
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
"""

if __name__ == "__main__":
    
    image = cv2.imread("./Assets/test3.jpg", 1)
    
    findColour(image, "red")
