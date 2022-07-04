import numpy as np
import cv2

video_cap = cv2.VideoCapture(0)
size_text = 2

while True:
    ret,frame = video_cap.read()
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faded = frame[200:300,300:400]
    if ret == False:
        break
 
    filter_camera = np.ones((35,35))/1225
    frame = cv2.filter2D(frame,-1,filter_camera)

    frame[200:300,300:400] = faded
    color_faded = frame[200:300,300:400]

    if  0 < np.average(color_faded) <= 85:
        cv2.rectangle(frame,(300,200), (400,300), (0, 0, 0),2)
        cv2.putText(frame,"Black",(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),int(size_text))
        
    elif 85 < np.average(color_faded) <= 170:
        cv2.rectangle(frame,(300,200), (400,300), (127, 127, 127),2)
        cv2.putText(frame,"gray",(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(127,127,127),int(size_text))
        
    elif 170 < np.average(color_faded) <= 255:
        cv2.rectangle(frame,(300,200), (400,300), (255, 255, 255),2)
        cv2.putText(frame,"white",(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255, 255, 255),int(size_text))
       
    cv2.imshow("faded",frame)
    cv2.waitKey(5)            