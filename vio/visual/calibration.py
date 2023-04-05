import cv2
import numpy as np
import glob

# termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + CV2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

chessboardSize = (7, 7)
frameSize = (640, 480)

objp = np.zeros((chessboardSize[0] * chessboardSize[1], 3), np.float32)

