import cv2

def get_moving_foreground(prev_frame, frame, next_frame):
    """
        Use Three Frame Difference Approach to get moving Foreground Object
        in one frame
        Reference this blog post:
            https://sam-low.com/opencv/frame-differencing.html
    """
    # get differences between frames to detect motion
    diff1 = cv2.absdiff(prev_frame, frame)
    diff2 = cv2.absdiff(frame, next_frame)
    
    # increase contrast between foreground and background by thresholding
    threshold_value = 10
    set_to_value = 255
    _, diff1 = cv2.threshold(diff1, threshold_value, set_to_value, cv2.THRESH_BINARY)
    _, diff2 = cv2.threshold(diff2, threshold_value, set_to_value, cv2.THRESH_BINARY)
    
    # find the overlap between the difference frames to get moving object
    overlap = cv2.bitwise_and(diff1, diff2)
    
    # use median filtering to fill some holes of the moving foreground
    overlap = cv2.medianBlur(overlap,5)
    
    return overlap