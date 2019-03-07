import cv2
import io
import time
from picamera import PiCamera
import cv2
import numpy as np
from findColour import findColour 

while True:
	# Create the in-memory stream
	stream = io.BytesIO()
	with PiCamera() as camera:
		camera.start_preview()
		time.sleep(2)
		camera.capture(stream, format='jpeg')
		camera.capture('/home/pi/RealWorldProject/MachineVision/Output/cam.jpg')
	# Construct a numpy array from the stream
	data = np.fromstring(stream.getvalue(), dtype=np.uint8)
	# "Decode" the image from the array, preserving colour
	#image = cv2.imdecode(data, 1)
	# OpenCV returns an array with data in BGR order. If you want RGB instead
	# use the following...
	
	image = cv2.imdecode(data, 1)
	findColour(image, True)
	input("Press enter for next frame.")