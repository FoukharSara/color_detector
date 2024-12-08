import numpy as np 
import cv2

def get_lim(color):
    
    c = np.uint8([[color]])
    hsvC = cv2.cvtColor(c,cv2.COLOR_BGR2HSV)
    hue_range = 10
    min_saturation = 50  
    
    #100 as min for saturation and brightness to avoid false detections, only yhose with enough dkshi
    lowerLimit = (max(hsvC[0][0][0] - hue_range, 0),  100, 100)  # HSV lower range
    upperLimit = (min(hsvC[0][0][0] + hue_range, 180), 255, 255)  # HSV upper range
    
    lowerLimit = np.array(lowerLimit, dtype=np.uint8)
    upperLimit = np.array(upperLimit, dtype=np.uint8)
    
    return lowerLimit, upperLimit