import numpy as np
import cv2

def findColour(filename, colour):
    """Function that takes path of an image and outputs a new file highlighting said colour."""
    if colour == "red":
        boundaries = [(0, 150, 50),(7, 255, 255)]  #pair of least red and most red on the hsv map 
        wrapAround = [(170, 150, 50), (180, 255, 255)] 
    elif colour == "green":
        boundaries = [(36, 25, 25), (80, 255,255)]

    image = cv2.imread(filename, 1) #gcolour
    
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    lower = boundaries[0]
    upper = boundaries[1]

    mask = cv2.inRange(hsv, lower, upper)
    
    if colour == "red":
        additionalMask = cv2.inRange(hsv, wrapAround[0], wrapAround[1])
        mask += additionalMask  #since they're nothing but arrays, we can simply add them together 
        
    output = cv2.bitwise_and(image, image, mask = mask) #highlights our mask onto the original image 
 
    cv2.imwrite('output.jpg', output)
    
if __name__ == "__main__":
    findColour("/home/codio/workspace/WheelieVehicle/Assets/test2.jpg", "red")