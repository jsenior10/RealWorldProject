import cv2
from findColour import findColour

while True:
	userInput = input("Image: ")

	for colour in ["red", "green"]:
		image = cv2.imread("./Assets/" + userInput + ".jpg", 1)
		findColour(image, colour)