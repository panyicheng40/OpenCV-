import os
import cv2
import numpy as np

ball_color1 = ['green', 'red', 'blue']
color = [(0, 0, 255), (255, 0, 0), (0, 255, 0)]  # 轮廓的对应标记颜色

color_dist = {'red': {'Lower': np.array([0, 60, 60]), 'Upper': np.array([6, 255, 255])},
              'blue': {'Lower': np.array([100, 80, 46]), 'Upper': np.array([124, 255, 255])},
              'green': {'Lower': np.array([35, 43, 35]), 'Upper': np.array([90, 255, 255])}}

path = "C:\\Users\\panyi\\Pictures"
dir1 = os.listdir(path)
for img in dir1:
    image = "C:\\Users\\panyi\\Pictures\\"+img
    img1 = cv2.imread(image)   # 读取图片
    if img1 is not None:
        for i in range(0,3):
            ball_color = ball_color1[i]
            gs_frame = cv2.GaussianBlur(img1, (5, 5), 0)                     # 高斯模糊
            hsv = cv2.cvtColor(gs_frame, cv2.COLOR_BGR2HSV)                 # 转化成HSV图像
            erode_hsv = cv2.erode(hsv, None, iterations=2)                   # 腐蚀 粗的变细
            inRange_hsv = cv2.inRange(erode_hsv, color_dist[ball_color]['Lower'], color_dist[ball_color]['Upper'])
            # 除去对应颜色形状之外的背景
            contours = cv2.findContours(inRange_hsv.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]  # 寻找轮廓
            img2 = cv2.drawContours(img1, contours, -1, color[i], 1)  # 绘制轮廓
        cv2.imshow('camera', img2)
        cv2.waitKey(0)
    else:
        print("无图片")