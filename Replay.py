import numpy as np
import imutils
import cv2

cap = cv2.VideoCapture("C:\\Users\\panyi\\Desktop\\Work\\FindContours\\data\\launch.mp4")

while(cap.isOpened()):

    ret, frame = cap.read()
    # frame = imutils.resize(frame, width=500)
    # cv2.namedWindow("Image", cv2.WND_PROP_FULLSCREEN)
    # cv2.setWindowProperty("window",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)

    if ret:
        frame = imutils.resize(frame, width=500)
        cv2.imshow("Image", frame)
    else:
       print('no video')
       cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()