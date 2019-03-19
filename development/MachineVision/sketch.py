import io
import time
import pigpio
from findColour import findColour
from picamera import PiCamera
import numpy as np
import cv2

print("Initalising..")

pin = 23
pi = pigpio.pi()
pi.set_mode(23,pigpio.OUTPUT)

def steering(value):
    pi.set_servo_pulsewidth(pin, value)

camera = PiCamera()
camera.resolution = (480, 240)
camera.start_preview()

lastCommand = 0

try:
    while True:
        stream = io.BytesIO()
        start = time.time()
        camera.capture(stream, format='jpeg', use_video_port=True)
        end = time.time()
        print("Amount of time to take picture ", end - start)
        data = np.fromstring(stream.getvalue(), dtype=np.uint8)

        image = cv2.imdecode(data, 1)
        maskRed, maskYellow = findColour(image, False)

        redCount = 0
        yellowCount = 0
        foundRed = False
        foundYellow = False
       # print( int(len(maskRed)*0.088)  , int( len( maskRed ) * 0.1) )

        for i in range(int(len(maskRed) * 0.892), int(len(maskRed) * 0.9)):
            for k in range(0, int(len(maskRed[i]) / 2)):  # looks at the left pixels
                if redCount > 25:
                    print("Red at position: ", positionRed)
                    foundRed = True
                    break
                if maskRed[i][k]:  # faster than == 255
                    if (not redCount):  # when count is 0
                        positionRed = k
                    redCount += 1

            for k in reversed(range(int(len(maskYellow[i]) / 2), len(maskYellow[i]))):  # right of image
                # reversed looks at the pixels right to left
                if yellowCount > 25:
                    print("Yellow at position: ", positionYellow)
                    foundYellow = True
                    break
                if maskYellow[i][k]:  # faster than == 255
                    if (not yellowCount):  # when count == 0
                        positionYellow = k
                    yellowCount += 1
        
        if not foundRed:
            positionRed = -100
        if not foundYellow:
            poisitionYellow = 500

        if foundRed or foundYellow: #functionally the same, more readable
            direction = 400 - positionYellow - positionRed
            
            if direction > 250:
                  direction = 250 #ensures we never go over our bounds
            elif direction < -250: #never under 
                  direction = -250
                    
            print("\nWe are this close: ", direction)
            
            if 30 > direction > -30:
                print("Dead on. Keep straight.")
                if lastCommand < 1450: 
                   direction = 100 #center changes based on where we came from
                elif lastCommand > 1550:
                   direction = 0
                
            elif direction >= 30:
                print("Turn left.")
            elif direction <= -30:
                print("Turn right")
         
            steering(1450 + direction) 
            lastCommand = 1450 + direction
            direction = 0
        else:
            print("Lost track of them. Next frame.")
        end = time.time()
        print("Total time spent on frame: ", end - start)
        #input()
except KeyboardInterrupt:
    pi.stop()
    steering(0)
steering(0)
pi.stop()
