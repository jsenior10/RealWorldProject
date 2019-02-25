import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)	#Sets the GPIO mode
GPIO.setup(23,GPIO.OUT)	#Pin 23 to be used and data out
pwm = GPIO.PWM(23,50)	#PWM mode for pin 23
pwm.start(7)


for i in range(0, 180):
    inputdegree=input("Input degree: ")	#Input for degree rotation
    DC=1./18.*(inputdegree) + 2			#Duty Cycle Equation
    pwm.ChangeDutyCycle(DC)				

pwm.stop()
GPIO.cleanup()