import cv2
from PIL import Image

from util import get_lim

yellow = [0,255,255] #aand this is yellooow in bgr colorspace
cap = cv2.VideoCapture(0)
while True:
    ret,frame = cap.read()
    if not ret:
        break
    
    hsvIm=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    lowerLimit,upperLimit = get_lim(color=yellow)
    
    #mask is actually grayscale 
    mask=cv2.inRange(hsvIm, lowerLimit,upperLimit)
    
    #convert from np array to pillow so that we can use getbbox
    mask_ = Image.fromarray(mask)
    
    bbox = mask_.getbbox()
    
    #print(bbox)
    if bbox is not None:
        x1,y1,x2,y2=bbox
        
        frame = cv2.rectangle(frame,(x1,y1),(x2,y2),(255,0,0),5)
        
    #this is aaaawesome
    # cv2.imshow('frame',mask)
    cv2.imshow('frame',frame) 
    
    if cv2.waitKey(25) == ord('q'):
        break
    

cap.release()
cv2.destroyAllWindows()