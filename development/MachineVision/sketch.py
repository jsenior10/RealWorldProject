import time
import RPi.GPIO as GPIO
import time
import cv2
import io
from picamera import PiCamera
#import picamera.array
import numpy as np
from findColour import findColour

def test():
  stream = io.BytesIO()
  data = np.fromstring(stream.getvalue(), dtype=np.uint8)
  image = cv2.imdecode(data,1)
  findColour(image, False)
  count = 0
  if maskRed == None:
    print("Didn't find red.")
    #continue
  exitProgram = False

  for i in range(int(len(maskRed)*0.6), int(len(maskRed)), 15):
    print("Counting pixels")
    for k in range(80,240): #for performance reasons
        pixel = maskRed[i][k]
        if pixel == 255:
            count += 1
        if count > 150:
            exitProgram = True
            break
    if exitProgram:
      break
    print("Didn't find red. Next frame")
GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
#stream = [io.BytesIO() for i in range(30)]
#stream = io.BytesIO()

steer = GPIO.PWM(16, 50)
speed = GPIO.PWM(18, 50)
print("initialising camera")
start = time.time()
camera = PiCamera()
camera.resolution = (480, 240)
#camera.framerate(30)
camera.start_preview()
end = time.time()
print("camera initialised - time taken ")
print(end - start)

#if input("Direction? ") == "l":
#	steer.start(15) #left
#else:
#	steer.start(1) #right

while True:
	userInput = input("Speed: ")
	if userInput == "next":
		break
	speed.start(float(userInput))

try:
  #print("In the future well try finding red here")
	while True:
			#camera.resolution = (720, 240)
			#camera.start_preview()
			#time.sleep(2)
		stream = io.BytesIO()
		#print("Taking picture")
		#input("Enter to take picture")
		#camera.start_preview()
		start = time.time()
		camera.capture(stream,format='jpeg', use_video_port=True)
		#camera.capture('./Output/cam.jpg', format='jpeg')
		end = time.time()
		#print("We have taken a picture")
		print("Amount of time to take picture ", end - start)
		data = np.fromstring(stream.getvalue(), dtype=np.uint8)

		image = cv2.imdecode(data,1)
		maskRed, maskYellow = findColour(image, False)

		count = 0
		#if maskRed == None:
			#print("Didn't find red.")
			#continue
		exitProgram = False
		start = time.time()
		#print("Lenght of maskRed, ", len(maskRed) )
		#input()
		print(int(len(maskRed)*0.87), int(len(maskRed)*0.9))
		redPositions = {}
		for i in range(int(len(maskRed)*0.892), int(len(maskRed)*0.9)):
			#print("Counting pixels ", len(maskRed[i]))
			#redPositions[i] = [None, None] 
			for k in range(0,int(len(maskRed[i])/2)): #for performance reasons
				#print(pixel, end=" ")
				if maskRed[i][k] == 255:
					if count == 0:
						position = k
					#if redPositions[i][0] == None:
					#	redPositions[i][0] = k
					#redPositions[i][1] = k
					lastRed = k
					count += 1
				#print("Current count: ", count)
			if count > 25:
				print(redPositions)
				#keys = list(redPositions.keys())
				size = lastRed - position #redPositions[max(keys)][1] - redPositions[min(keys)][0]
				#position = #redPositions[min(keys)][0]
				print("Size(px): ", size)
				print("At position: ", position)
				print("Current red pixel count: ", count)
				exitProgram = True
				break
		if exitProgram:
			break
		end = time.time()
		print("Didn't find red. Next frame")
		print("Processing time: ", end - start)

except(KeyboardInterrupt):
  GPIO.cleanup()

GPIO.cleanup()
