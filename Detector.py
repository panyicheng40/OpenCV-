import argparse
import imutils
import cv2
import numpy
import time
import datetime

# 创建参数解析器并解析参数
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help="path to the video file")
ap.add_argument("-a", "--min-area", type=int, default=500, help="minimum area size")
args = vars(ap.parse_args())

# 读取视频文件
camera = cv2.VideoCapture("C:\\Users\\panyi\\Desktop\\Work\\视频\\原视频\\00000002869000000.mp4")

# 初始化视频流的帧变量
gray = None
blank = None

# 遍历视频的每一帧
while True:

    # 获取当前帧并初始化状态信息
    (grabbed, frame) = camera.read()
    text = "Unoccupied"
    isBlank = True

    # 备份一遍原视频文件
    (grabbed, original) = camera.read()

    # 视频播放完，结束循环
    if not grabbed:
        break

    # 在调整当前帧前存储前一帧
    prev_Frame = gray

    # 调整该帧的大小，转换为灰阶图像并高斯模糊
    frame = imutils.resize(frame, width=500)
    original = imutils.resize(original, width=500)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    # 如果前一帧是None，从下一帧开始抓取
    if prev_Frame is None:
        continue

    # 计算当前帧和前一帧的不同
    if blank is None:
        frameDelta = cv2.absdiff(prev_Frame, gray)
        thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]
    # 计算当前帧和背景帧的不同
    else:
        frameDelta = cv2.absdiff(blank, gray)
        thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]

    # 扩展阀值图像填充孔洞，然后找到阀值图像上的轮廓
    thresh = cv2.dilate(thresh, None, iterations=2)
    if blank is None:
        (contours, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    else:
        (contours, _) = cv2.findContours(blank.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 遍历轮廓
    for c in contours:

        # 遍历轮廓
        if cv2.contourArea(c) < args["min_area"]:
            continue

        # 填充所有的轮廓
        frame = cv2.drawContours(frame, contours, -1, (0, 0, 255), cv2.FILLED)

        # 计算轮廓的边界框，在当前帧中画出该框，并且更新标签
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        text = "Occupied"
        isBlank = False

    # 在当前帧上写文字
    cv2.putText(frame, "Room Status: {}".format(text), (5, 275), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    # 在当前帧上写时间戳
    # cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
    # (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)

    # 显示当前帧并记录用户是否按下按键
    cv2.imshow("Original", original)
    cv2.imshow("Security Feed", frame)
    cv2.imshow("Thresh", thresh)
    cv2.imshow("Frame Delta", frameDelta)
    key = cv2.waitKey(1) & 0xFF

    # 如果q键被按下，跳出循环
    #  if key == ord("q"):break

# 清理摄像机资源
camera.release()
