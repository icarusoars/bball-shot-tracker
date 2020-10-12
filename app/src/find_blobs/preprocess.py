import cv2

def preprocess_vid_frame(frame):
    """
        Do some preprocessing work on a frame of a video to 
        make it ready for image processing techniques.
        1) Convert frame to grayscale
        2) Apply gaussian blur to get rid of noise
    """
    # convert frame to grayscale
    new_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # gaussian blur with 5x5 kernel
    new_frame = cv2.GaussianBlur(new_frame,(5,5), 0)
    
    return new_frame