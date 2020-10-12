import cv2
import imutils

def get_blobs(frame, output):
    """
        Get all the blobs (connected components of white pixels)
        in a thresholded black and white image
        
        Reference: https://www.pyimagesearch.com/2015/05/25/
                   basic-motion-detection-and-tracking-with-python-and-opencv/
                   
        Blobs info is a list of dictionaries containing coordinates
        and size of blobs
    """
    
    cnts = cv2.findContours(frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    
    blobs_info = []
    
    # loop over the contours
    for c in cnts:
        # if the contour is too small, ignore it
        if cv2.contourArea(c) < 100:
            continue
            
        # find the bounding box for the contour
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(output, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # store blobs information into list of dictionaries
        b_info = {}
        b_info['x'], b_info['y'] = x, y
        b_info['width'], b_info['height'] = w, h
        
        blobs_info.append(b_info)
    
    return output, blobs_info