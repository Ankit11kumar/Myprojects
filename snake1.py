import numpy as np
import pandas as pd
import matplotlib as plt
import random as rd
import time as t
import cv2


z=np.zeros([400,400])
z[200:210,200:210]=255
x=rd.randint(0,400)
y=rd.randint(0,400)
z[x:x+10,y:y+50]=255
x1=[x,x+10]
y1=[y+40]
i=0;j=0
k=cv2.waitKey(0)
while(k!=ord('q')):
    k=cv2.waitKey(0)
    
    if(k==ord('w')):
        x=x-10
        x1.append(x)
        z[x1[i]:x1[i]+10,y1[j]:y1[j]+10]=0
        i=i+1
    elif(k==ord('a')):
        y=y-10
        y1.append(y)
        z[x1[i],y1[j]]=0
        j=j+1
        
    elif(k==ord('d')):
        y=y+10
        y1.append(y)
        z[x1[i],y1[j]]=0
        j=j+1
        
    elif(k==ord('s')):
        x=x+10
        x1.append(x)
        z[x1[i],y1[j]]=0
        i=i+1
        
    z[x:x+10,y:y+10]=255
    cv2.imshow('image',z)
   
