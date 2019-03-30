import cv2,time
v=cv2.VideoCapture(0)
time.sleep(2)
f=cv2.CascadeClassifier(r'C:\Program Files (x86)\Python36-32\Lib\site-packages\cv2\data\haarcascade_frontalface_alt.xml')
while(1):
    r,i=v.read()
    j=cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)
    fd=f.detectMultiScale(j,1.3,7)
    l=len(fd)
    print('No. of faces are:',l)
    for(x,y,w,h) in fd:
        cv2.rectangle(i,(x,y),(x+w,y+h),(0,0,255),3)
    cv2.imshow('face',i)
    k=cv2.waitKey(1)
    if(k==ord('q')):
        break
