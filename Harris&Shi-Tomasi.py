import numpy as np
import cv2
import imutils
from matplotlib import pyplot as plt

# 读取图片文件
img = cv2.imread('C:\\Users\\panyi\\Pictures\\Capture\\example1.jpg')

# 调整图片尺寸
img = imutils.resize(img, width=500)

# 备份图片
imgShi, imgHarris = np.copy(img), np.copy(img)

# 转换成灰度图
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Shi-Tomasi角点检测
# 速度相比Harris有所提升，可以直接得到角点坐标
corners = cv2.goodFeaturesToTrack(gray, 20, 0.01, 10)
corners = np.int0(corners)

# 压缩至一维：[[62, 64]] -> [62, 64]
for i in corners:
    x, y = i.ravel()
    cv2.circle(imgShi, (x, y), 4, (0, 0, 255), -1)

# Harris角点检测
dst = cv2.cornerHarris(gray, 2, 3, 0.04)

# 腐蚀一下，便于标记
dst = cv2.dilate(dst, None)

# 角点标记为红色
imgHarris[dst > 0.01 * dst.max()] = [0, 0, 255]

cv2.imwrite('compare.png', np.hstack((imgHarris, imgShi)))
cv2.imshow('compare', np.hstack((imgHarris, imgShi)))
cv2.waitKey(0)
