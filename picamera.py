# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2


#modulename = input('process_local.py')
#import_module(modulename)

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.startPreview()

sleep(5)

camera.capture('./img.jpg')

camera.stopPreview()
