import numpy as np
import matplotlib as plt
import cv2
from pynput.mouse import Button,Controller

mouse=Controller()
v=cv2.VideoCapture(0)

while(1):
    r,i=v.read()
    j=cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)
    p=i[:,:,1]
    d=cv2.subtract(p,j)
    r1,k=cv2.threshold(d,10,255,0)
    M = cv2.moments(k)
    if(M["m00"]!=0):
        cx = int(M["m10"] / M["m00"])
        cy = int(M["m01"] / M["m00"])
    mouse.position = (cx,cy)
    
    image,contours,hierarchy = cv2.findContours(k,1,2)  # contours means white patches..will return array of contours.
    c=0
    for s in range(0,len(contours)):
        area = cv2.contourArea(contours[s])
        if(area>500): 
            mouse.press(Button.left)
        if(area>800):
            mouse.release(Button.left)
            
    k=cv2.waitKey(1)
    if(k==ord('q')):
        cv2.destroyAllWindows()
        v.release()
        break
   
