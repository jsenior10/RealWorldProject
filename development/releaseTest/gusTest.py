import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD) #board numbering system
GPIO.setup(16, GPIO.OUT) #output pin numbers
GPIO.setup(18, GPIO.OUT)

servo = GPIO.PWM(16, 50)
motor = GPIO.PWM(18, 50)
t = time.sleep

def servoAllign():
	servo.start(15)
	time.sleep(.5)
	servo.start(1)
	time.sleep(.5)
	servo.start(6.85)
	time.sleep(.5)

def changeServo(direction):
	if direction == "l":
		servo.start(15)
	if direction == "r":
		servo.start(1)
	if direction == "m":
		servo.start(6.85)


def changeSpeed(speed):
	motor.start(float(speed))


def slowRight():
	changeSpeed(7.80)
	changeServo("r")
	t(0.5)
	changeServo("m")
	t(0.5)
	changeServo("r")
	t(0.5)
	changeServo("m")
	t(0.5)
	changeServo("r")
	t(0.5)
	changeServo("m")
	t(0.2)

def main():
	servoAllign()
	slowRight()
	GPIO.cleanup()

main()
