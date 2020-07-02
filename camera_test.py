import numpy as np
import cv2
import matplotlib.pyplot as plt

#for video capture through the camera, it has to go through the gStreamer by invoking the correct command
#below is the command for the econ systems camera See3CAM_CU30
cap=cv2.VideoCapture("v4l2src device=/dev/video1 ! video/x-raw, width=(int)1280, height=(int)720, format=UYVY ! videoconvert ! video/x-raw, format=RGB ! videoconvert !appsink", cv2.CAP_GSTREAMER)

while(True):
  ret, frame=cap.read()
  #gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  
  cv2.imshow("Web cam",frame)
  cv2.imshow("grayscale video",frame)
  # When we press Q on our keyboard we will exit a video
  if cv2.waitKey(1) & 0xFF == ord('q'):
      break
# Release the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()

