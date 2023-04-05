import cv2
import numpy as np
import glob

# termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + CV2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

chessboardSize = (7, 7)
frameSize = (640, 480)

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((chessboardSize[0] * chessboardSize[1], 3), np.float32)
objp[:,:2] = np.mgrid[0:7,0:6].T.reshape(-1,2)

# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpointsL = [] # 2d points in left image plane.
imgpointsR = [] # 2d points in right image plane.

left_images = glob.glob('images/left/*.png')
right_images = glob.glob('images/right/*.png')

for (imgL_fname, imgR_fname) in zip(left_images, right_images):
    imgL = cv2.imread(imgL_fname)
    imgR = cv2.imread(imgR_fname)
    grayL = cv2.cvtColor(imgL, cv2.COLOR_BGR2GRAY)
    grayR = cv2.cvtColor(imgR, cv2.COLOR_BGR2GRAY)

    if cv2.checkChessboard(imgL) and cv2.checkChessboard(imgR):

        # find chessboard corners
        _, cornersL = cv2.findChessboardCorners(grayL, chessboardSize, cv2.CALIB_CB_FAST_CHECK)
        _, cornersR = cv2.findChessboardCorners(grayR, chessboardSize, cv2.CALIB_CB_FAST_CHECK)

        objpoints.append(objp)
        cornersL2 = cv2.cornerSubPix(grayL, cornersL, (11,11), (-1,-1), criteria)
        cornersR2 = cv2.cornerSubPix(grayR, cornersR, (11,11), (-1,-1), criteria)
        imgpointsL.append(cornersL2)
        imgpointsR.append(cornersR2)

        # Draw and display corners
        cv2.drawChessboardCorners(imgL, chessboardSize, cornersL2, True)
        cv2.drawChessboardCorners(imgR, chessboardSize, cornersR2, True)
        cv2.imshow('Image with corners', imgL)
        cv2.imshow('Image with corners', imgR)
        cv2.waitKey(5)

cv2.destroyAllWindows()

ret, cameraMatrixL, distL, cameraMatrixR, distR, rvecs, tvecs, essentialMatrix, fundamentalMatrix = cv2.stereo