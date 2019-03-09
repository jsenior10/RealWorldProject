import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD) #board numbering system
GPIO.setup(16, GPIO.OUT) #output pin numbers
GPIO.setup(18, GPIO.OUT)

servo = GPIO.PWM(16, 50)
motor = GPIO.PWM(18, 50)


def changeServo(direction):
	if direction == "l":
		servo.start(15)
	if direction == "r":
		servo.start(1)
	if direction == "s":
		servo.start(8)


def changeSpeed(speed):
	motor.start(float(speed))


def main():
	while True:
		direction = input("\nplease enter l, s or r: ")
		speed = input("please enter speed 7.00-9.00: ")
		changeServo(direction)
		changeSpeed(speed)
	GPIO.cleanup()

main()
