import cv2 as cv
from time import time
from time import sleep
from vision import Vision
from windowcapture import WindowCapture
import mouse

#C:\opencv3.4\opencv\build\x64\vc14\bin\opencv_traincascade.exe -data cascade/ -vec pos.vec -bg neg.txt -w 24 -h 24 -numPos 73 -numNeg 82 -numstages 4C:\opencv3.4\opencv\build\x64\vc14\bin\opencv_traincascade.exe -data cascade/ -vec pos.vec -bg neg.txt -w 24
# initialize the WindowCapture class
wincap = WindowCapture('Roblox')

loop_time = time()
cascade_fish = cv.CascadeClassifier('cascade/cascade.xml')
vision_fish = Vision(None)

while(True):

    screenshot = wincap.get_screenshot()
    rectangles = cascade_fish.detectMultiScale(screenshot)
    if len(rectangles) >= 4:
        mouse.click('left')
        sleep(5)
        mouse.click('left')

    #detected = vision_fish.draw_rectangles(screenshot, rectangles)
    
    #cv.imshow('Fishing', detected)

    print('FPS {} - {}'.format(1 / (time() - loop_time), len(rectangles)))
    loop_time = time()
    key = cv.waitKey(1)
    if key == ord('q'):
        cv.destroyAllWindows()
        break
    #elif key == ord('f'):
        cv.imwrite('positive2/{}.jpg'.format(loop_time),screenshot)
    #elif key == ord('g'):
        cv.imwrite('negative2/{}.jpg'.format(loop_time),screenshot)
