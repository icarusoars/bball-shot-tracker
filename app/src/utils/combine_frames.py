import numpy as np
import cv2
import imutils

def combine_frames(grid_size, frames, combined_width):
    """
        Expects frames to be a dictionary mapping grid location to frame
        (0,0)  (0,1)  (0,2)
        (1,0)  (1,1)  (1,2)
        Expects all frames to be same dimensions and have same number of color chanels
    """
    color_chanels = frames[(0,0)].shape[2]
    height, width = frames[(0,0)].shape[0], frames[(0,0)].shape[1]
    
    combined_frame = np.zeros((height * grid_size[0],
                               width  * grid_size[1],
                               color_chanels), dtype = "uint8")
    
    for (grid_r, grid_c), frame in frames.items():
        combined_frame[grid_r * height : (grid_r + 1) * height,
                       grid_c * width  : (grid_c + 1) * width , : ] = frame
    
    combined_frame_resized = imutils.resize(combined_frame, width=combined_width)
#     cv2.imshow(combined_frame_resized)
    
    return combined_frame_resized


"""Example usecase
frames = {
    (0,0) : image,
    (0,1) : image
}
combined = combine_frames(grid_size = (2,3), frames = frames, combined_width = 1500)

cv2.imshow("Combined frames", combined)
"""