import io
import time
import pigpio
from findColour import findColour
from picamera import PiCamera
from picamera.array import PiRGBArray
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

lastCommand = 1500 #starts middle 

try:
    while True:
        start = time.time()
       
        #stream = io.BytesIO()
        #camera.capture(stream, format='jpeg', use_video_port=True)
        #data = np.fromstring(stream.getvalue(), dtype=np.uint8)
        #image = cv2.imdecode(data, 1)
        
        with picamera.array.PiRGBArray(camera) as stream:
            camera.capture(stream, format='bgr')
            image = stream.array 
            
        end = time.time()   
        print("Amount of time to take picture ", end - start)
        
        maskRed, maskYellow = findColour(image, False)

        redCount = 0
        yellowCount = 0
        foundRed = False
        foundYellow = False

        for i in range(int(len(maskRed) * 0.892), int(len(maskRed) * 0.9)):
            #iterates vertically over slices 
            for k in range(0, int(len(maskRed[i]) / 2)):  # looks at the left pixels
               #pixel by pixel horizontally
                if maskRed[i][k]:  # faster than == 255
                    if (not redCount):  # when count is 0
                        positionRed = k                     
                    redCount += 1       
                    if redCount > 25:
                        print("Red at position: ", positionRed)
                        foundRed = True
                        break
                        
            for k in reversed(range(int(len(maskYellow[i]) / 2), 401)):  # right of image
               #pixel by pixel     #401 because last 80 pixels are not centered properly
                if maskYellow[i][k]:  # faster than == 255
                    if (not yellowCount):  # when count == 0
                        positionYellow = k
                    yellowCount += 1
                    if yellowCount > 25:
                        print("Yellow at position: ", positionYellow)
                        foundYellow = True
                        break
        
        if not foundRed:
            positionRed = -50 
        if not foundYellow:  #softer turn if cone not in field of view
            poisitionYellow = 450

        if foundRed or foundYellow: #functionally the same, more readable
            direction = 400 - positionYellow - positionRed
            
            if direction > 250:
                  direction = 250 #ensures we never go over our bounds
            elif direction < -250: #never under 
                  direction = -250
                    
            print("\nCurrent Direction: ", direction)
            
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
         
            if 1450+direction < lastCommand:
                steering(lastCommand - 25) #small increments
                lastCommand -= 25 
            else:
                steering(lastCommand + 25)
                lastCommand += 25 
            
            #steering(1450 + direction) 
            
        else:
            print("Lost track of cones. Next frame.")
            
        end = time.time()
        print("Total time spent on frame: ", end - start)
        #input()
        
except KeyboardInterrupt:
    if lastCommand < 1450: 
       steering(1550)
    elif lastCommand > 1550: #Resets to middle 
       steering(1450)
    else:
       steering(1500)
    pi.stop()

