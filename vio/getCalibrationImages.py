import cv2
import os

cap = cv2.VideoCapture(0)

while not cv2.isOpened():
    pass

num = 0
if not os.path.exists('images/left/'):
    os.mkdir('images/left/')
if not os.path.exists('images/right/'):
    os.mkdir('images/right/')

while True:
    ret, frame = cap.read()

    h, w, _ = frame.shape

    imgL = frame[:, :w]
    imgR = frame[:, w+1:]

    k = cv2.waitKey(5)

    if k == 27:
        break
    elif k == ord('s'):
        cv2.imwrite('images/left/' + str(num) + '.png', imgL)
        cv2.imwrite('images/right/' + str(num) + '.png', imgL)
        print('images saved')
        num += 1

    cv2.imshow("Left Image", imgL)
    cv2.imshow("Right Image", imgR)

