import numpy as np
import cv2

v=cv2.VideoCapture(0)
while(1):
    r,i=v.read()
    j=cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)
    r,k=cv2.threshold(j,180,255,1) #180 is threshold to be replaced by 255 i.e white..so all objects will turn to white and rest black.
    image,contours,hierarchy = cv2.findContours(k,1,2)  # contours means white patches..will return array of contours.
    for s in range(0,len(contours)):
        area = cv2.contourArea(contours[s])
        if(area>800): 
            print('Object detected')
    k=cv2.waitKey(5)
    if(k==ord('q')):
        break
#print(contours,area,hierarchy)
#print('no. of objects in the image--\n',c)
#cv2.imshow('image',k)
    
