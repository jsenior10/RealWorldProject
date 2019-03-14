import time
import RPi.GPIO as GPIO
import cv2
import io
from picamera import PiCamera
import numpy as np
from findColour import findColour

GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.OUT)
speed = GPIO.PWM(18, 50)

print("initialising camera")
start = time.time()

camera = PiCamera()
camera.resolution = (480, 240)
camera.start_preview()

end = time.time()
print("camera initialised - time taken ", end-start)

while True:
	userInput = input("Speed: ")
	if userInput == "next":
		break
	speed.start(float(userInput))

try:
	while True:
		stream = io.BytesIO()
		start = time.time()
		camera.capture(stream,format='jpeg', use_video_port=True)
		end = time.time()
		print("Amount of time to take picture ", end - start)
		data = np.fromstring(stream.getvalue(), dtype=np.uint8)

		image = cv2.imdecode(data,1)
		maskRed, maskYellow = findColour(image, False)

		redCount = 0
		yellowCount = 0 
		foundRed = False 
		foundYellow = False 

		for i in range(int(len(maskRed)*0.892), int(len(maskRed)*0.9)):
			for k in range(0,int(len(maskRed[i])/2)): #looks at the left pixels 
				if !foundRed and maskRed[i][k]: #faster than == 255
					if !redCount : #when count is 0 
						positionRed = k
					redCount += 1
	   	   	  
			for k in reversed(range(int(len(maskYellow[i])/2), len(maskYellow[i]))): #right of image 
	   	   	     #reversed looks at the pixels right to left 
				if !foundYellow and maskYellow[i][k]: #faster than == 255 
					if !yellowCount: #when count == 0 
						positionYellow = k
					yellowCount += 1   

			if redCount > 25:
				print("Red at position: ", positionRed)
				#print("Red pixel count: ", count)
				foundRed = True

			if yellowCount > 25:
				print("Yellow at position: ", positionYellow)
				#print("Yellow pixel count: ", count)
				foundYellow = True

		if foundRed and foundYellow:
			direction = 480-positionYellow-positionRed
			
			print("\nWe are this close: ", direction)
			if direction < 15 and direction > -15:
				print("Dead on. Keep straight.")
			elif direction > 100:
				print("Turn left.")
			elif direction < -100:
				print("Turn right")
			elif direction < -50:
				print("Almost there! Tiny bit left!")
			elif direction > 50: 
				print("Almost there! Tiny bit right!")

		end = time.time()
		print("Total time spent on frame: ", end - start)

except(KeyboardInterrupt):
	GPIO.cleanup()

GPIO.cleanup()
