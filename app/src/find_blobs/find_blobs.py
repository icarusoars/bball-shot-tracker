import cv2
from collections import deque
import numpy as np
import pandas as pd 
import streamlit as st
import matplotlib.pyplot as plt
import time

from .get_blobs import get_blobs
from .open_close import opening, closing
from .three_frame_motion import get_moving_foreground
from .preprocess import preprocess_vid_frame
from ..utils.combine_frames import combine_frames


def find_blobs(video, blob_frame):
    # record the last 3 frames of video for foreground detection
    frames = deque()
    frames.append(video.read()[1])
    frames.append(video.read()[1])
    frames.append(video.read()[1])


    # record blobs information
    blobs_info = []

    frame_count = 0
    while(video.isOpened()):
        frame_count += 1

        # current frame of consideration is the middle frame in frames deque
        cur_frame = frames[1]
        cur_frame = preprocess_vid_frame(cur_frame)

        # find moving foreground
        foreground = get_moving_foreground(preprocess_vid_frame(frames[0]), 
                                           preprocess_vid_frame(frames[1]),
                                           preprocess_vid_frame(frames[2]))
        
        
        # use closing technique to "close up" blobs
        foreground = opening(foreground)
        foreground = closing(foreground)
        


        # find blobs and record blobs information
        blobs_frame = cv2.cvtColor(cur_frame, cv2.COLOR_GRAY2RGB)
        blobs_frame, frame_blobs_info = get_blobs(foreground, blobs_frame)
        
        # frame_blobs_info contains all information of blobs for current frame
        frame_blobs_info = [{**{'frame_idx': frame_count}, **fbi} for fbi in frame_blobs_info]
        blobs_info.extend(frame_blobs_info)


        f = {
            (0,0): frames[1],
            (0,1): cv2.cvtColor(foreground, cv2.COLOR_GRAY2BGR),
            (1,0): blobs_frame
        }
        r = combine_frames((2,2), f, 1600)
        yield r
        # blob_frame.pyplot(fig = fig)

        # blob_frame.image(r, channels="BGR", use_column_width = True)
        # time.sleep(0.01)
        # cv2.imshow('Original & Foreground', r)


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # get next frame
        frames.popleft()
        ret, next_frame = video.read()
        if ret == False:
            break
        frames.append(next_frame)
        
        
    
    width  = video.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)
    
    video.release()
    cv2.destroyAllWindows()
    cv2.waitKey(1)

    blobs_df = pd.DataFrame(blobs_info)
    
    return blobs_df, (width, height)