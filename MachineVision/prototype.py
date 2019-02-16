from findColour import findColour

while True:
	userInput = input("Image: ")
	
	for colour in ["red", "green"]:
		findColour("./Assets/" + userInput + ".jpg", colour)