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
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # gray = cv2.GaussianBlur(gray, (21, 21), 0)

    # Shi-Tomasi角点检测
    corners = cv2.goodFeaturesToTrack(gray, 20, 0.01, 10)
    corners = np.int0(corners)  # 20 个角点坐标

    for i in corners:
        # 压缩至一维：[[62, 64]] -> [62, 64]
        x, y = i.ravel()
        cv2.circle(frame, (x, y), 4, (0, 0, 255), -1)

    # 角点标记为红色并显示当前帧
    cv2.imshow('DST', frame)
    key = cv2.waitKey(1) & 0xFF

# 清理摄像机资源
video.release()
