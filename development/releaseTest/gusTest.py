import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD) #board numbering system
GPIO.setup(16, GPIO.OUT) #output pin numbers
GPIO.setup(18, GPIO.OUT)

servo = GPIO.PWM(16, 50)
motor = GPIO.PWM(18, 50)

print("\nLeft or right?(l/r): ")
print("Motor range: 7.00 - 9.00, Vslow - Vfast\n")

try:
	while True:
		servoInput = input("Servo: ")
		motorInput = input("motor: ")

		if servoInput == "l":
			servo.start(15)
		if servoInput == "r":
			servo.start(1)
		else:
			print("Invalid servo input")

		motor.start(float(motorInput))

finally:
	GPIO.cleanup()
