"""
ECE196 Face Recognition Project
Author: W Chen

Adapted from:
http://www.pyimagesearch.com/2015/03/30/accessing-the-raspberry-pi-camera-with-opencv-and-python/

Use this code as a template to process images in real time, using the same techniques as the last challenge.
You need to display a gray scale video with 320x240 dimensions, with box at the center
"""


# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2


#modulename = input('process_local.py')
#import_module(modulename)

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
#camera.capture(rawCapture,'rgb',resize=(100,100))
# allow the camera to warmup
time.sleep(0.1)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

i=101
# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # grab the raw NumPy array representing the image, then initialize the timestamp
    # and occupied/unoccupied text
    image = frame.array

    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image=cv2.resize(image,(160,120))
    faces = face_cascade.detectMultiScale(image, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),(255,255,255),2)
        roi_gray = image[y:y+h, x:x+w]
        if i<400:
            cv2.imwrite('./umut/img%s.jpg' % i, roi_gray)
            i=i+1
            print i
    #height, width=image.shape
    #cv2.rectangle(image,(width/2-50,height/2-50),(width/2+50,height/2+50),(255,255,255),2)

    # show the frame
    cv2.imshow("Frame", image)
    key = cv2.waitKey(1) & 0xFF

    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break
