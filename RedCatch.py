import cv2
import argparse
import numpy as np
import imutils

# 设置字体
font = cv2.FONT_HERSHEY_SIMPLEX

# 创建参数解析器并解析参数
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help="path to the video file")
ap.add_argument("-a", "--min-area", type=int, default=500, help="minimum area size")
args = vars(ap.parse_args())

# 读取视频文件
video = cv2.VideoCapture("C:\\Users\\panyi\\Desktop\\Work\\视频\\实验视频\\晴天背光 左上 慢速 标清.mp4")
# video = cv2.VideoCapture("C:\\Users\\panyi\\Desktop\\Work\\视频\\原视频\\00000002704000000.mp4")

# 遍历视频的每一帧
while True:

    # 获取当前帧并初始化状态信息
    ret, frame = video.read()

    # 视频播放完，循环播放
    if not ret:
        print('Video Replay')
        video.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue

    # 调整视频尺寸
    frame = imutils.resize(frame, width=500)

    # 获取图片HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 红色范围低阈值169, 100, 100, 高阈值189, 255, 255
    lower_range = np.array([169, 100, 100])
    upper_range = np.array([189, 255, 255])

    # 根据颜色范围删选
    mask = cv2.inRange(hsv, lower_range, upper_range)

    # 中值滤波
    mask = cv2.medianBlur(mask, 7)

    cv2.imshow('image', frame)
    cv2.imshow('mask', mask)
    key = cv2.waitKey(1) & 0xFF

# 清理摄像机资源
video.release()
