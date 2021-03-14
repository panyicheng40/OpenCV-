import argparse
import imutils
import cv2
import numpy as np

# 创建参数解析器并解析参数
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help="path to the video file")
ap.add_argument("-a", "--min-area", type=int, default=500, help="minimum area size")
args = vars(ap.parse_args())

# 读取视频文件
# video = cv2.VideoCapture("C:\\Users\\panyi\\Desktop\\Work\\视频\\实验视频\\晴天背光 左上 慢速 标清.mp4")
video = cv2.VideoCapture("C:\\Users\\panyi\\Desktop\\Work\\视频\\原视频\\00000002704000000.mp4")

# 遍历视频的每一帧
while True:

    # 获取当前帧并初始化状态信息
    ret, frame = video.read()

    # 视频播放完，循环播放
    if not ret:
        print('Video Replay')
        video.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue

    # 调整该帧的大小，转换为灰阶图像(并不需要高斯模糊)
    frame = imutils.resize(frame, width=500)
    # frame = cv2.blur(frame, ksize=(5, 11))

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # gray = cv2.GaussianBlur(gray, (21, 21), 0)


    # Harris角点检测
    dst = cv2.cornerHarris(gray, 2, 3, 0.04)
    # 腐蚀一下，便于标记
    dst = cv2.dilate(dst, None)

    # 角点标记为红色并显示当前帧
    frame[dst > 0.01 * dst.max()] = [0, 0, 255]
    cv2.imshow('DST', frame)
    key = cv2.waitKey(1) & 0xFF

# 清理摄像机资源
video.release()

