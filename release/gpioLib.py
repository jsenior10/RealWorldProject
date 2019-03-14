import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)  # Pins on the board are numbered, GPIO.BOARD
# uses these numbers to refer to correct pins.

SERVO = 23  # Pin numbers for servo and motor.
MOTOR = 24

# GPIO.setmode(GPIO.BCM)         #alternate pin numbering system.
# GPIO.setwarnings(False)        #disables script warnings if pin has been
# configured for another value.

GPIO.setup(SERVO, GPIO.OUT)  # Sets GPIO pins up for outputting signals
GPIO.setup(MOTOR, GPIO.OUT)  # for the servo and motor.


def motorPower():
    p = GPIO.PWM(MOTOR, 2)
    p.start(1)
    p.stop()
    return 0


def servoPower():
    return 0


GPIO.cleanup(SERVO)  # END of program to clean GPIO pins this stops
GPIO.cleanup(MOTOR)  # shorting of pins on the board.
