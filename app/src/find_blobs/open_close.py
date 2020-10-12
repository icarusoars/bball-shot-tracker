import cv2
import numpy as np

def opening(frame):
    
    kernel = np.ones((5,5),np.uint8)
    closing = cv2.morphologyEx(frame, cv2.MORPH_OPEN, kernel)
    
    return closing

def closing(frame):
    
    kernel = np.ones((15,15),np.uint8)
    closing = cv2.morphologyEx(frame, cv2.MORPH_CLOSE, kernel)
    
    return closing