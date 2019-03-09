import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

steer = GPIO.PWM(16, 50)
speed = GPIO.PWM(18, 50)


if input("Direction? ") == "l":
	steer.start(15) #left
else:
	steer.start(1) #right

while True:
	userInput = input("Speed: ")
	if userInput == "next":
		break
	speed.start(float(userInput))

try:
	print("In the future well try finding red here")
	#while True:
		#if findColour("red"):
			#speed.start(7) #stops the car

except(KeyboardInterrupt):
	GPIO.cleanup()

GPIO.cleanup()
