import numpy as np
import cv2
import time
import os
import sys
import requests
import base64
import json

capture_duration = 10
FILE_OUTPUT = 'output/frames'
FILE_OUTPUT_V = 'output/video/output.avi'

# Checks and deletes a previously existing output.avi file 
# as there cant be a file with the same name or it will through an error
# if os.path.isfile(FILE_OUTPUT):
#     os.remove(FILE_OUTPUT)

#print("Before URL")

# cap = cv2.VideoCapture('rtsp://admin:123456@192.168.1.10/stream=1&subtype=0')
# cap = cv2.VideoCapture('rtsp://admin:admin1357@96.75.27.118:554/live/view.php',cv2.CAP_GSTREAMER)
# cap = cv2.VideoCapture('http://admin:admin1357@192.168.1.10:')

def accessCamera(username,password,rtspUrl):
    # url = 'rtsp://username:password@75.148.79.126:554/stream=1'
    url = 'rtsp://'+ username + ':' + password + '@' + rtspUrl + '/stream=1'

    camera = cv2.VideoCapture(url)
    
    fr=0

    # Get current width of frame
    width = camera.get(cv2.CAP_PROP_FRAME_WIDTH)   # float

    # Get current height of frame
    height = camera.get(cv2.CAP_PROP_FRAME_HEIGHT) # float

     # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(FILE_OUTPUT_V,fourcc, 20.0, (800,500))
    start_time = time.time()
    while( int(time.time() - start_time) < capture_duration ):
    # while(camera.isOpened())
        # fr=fr+1
        
        # camera.set(cv2.CAP_PROP_POS_MSEC,(fr*1000))   # assigns frame saving for every 1 sec
    
        check,frame=camera.read()

        # hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
        # out.write(frame)

        # print(check)
        # print(frame)

        if check == True:
            # frame = cv2.flip(frame,0)
            out.write(frame)
         #saves image
            # cv2.imwrite( FILE_OUTPUT + "\\frame%d.jpg" % fr, hsv)    # for wrinting the gray scale frames
            cv2.imwrite( FILE_OUTPUT + "\\frame%d.jpg" % fr, frame)

            cv2.imshow("capturing",frame)
            # cv2.imwrite("frame%d.jpg" % fr, frame)
            # cv2.imshow("video",hsv)

        else:
            break
        if cv2.waitKey(1000) & 0xFF == ord('q'):
            break

        fr=fr+1
        # key=cv2.waitKey(3000)
        # if key == ord('q'):
        #     break

    print(fr) 

    camera.release()

    out.release()

    cv2.destroyAllWindows

accessCamera('admin','Ditto2020!','75.148.79.126:554')
# accessImageFromLocation()

# camera.release()
# cv2.destroyAllWindows
# start_time = time.time()
# while( int(time.time() - start_time) < capture_duration ):
#     ret, frame = cap.read()
#     if ret==True:
#         frame = cv2.flip(frame,0)
#         out.write(frame)
#          cv2.imshow('frame',frame)
#     else:
#         break