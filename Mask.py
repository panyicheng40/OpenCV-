import cv2
import numpy as np

# 以灰度方式读取图像
img = cv2.imread("C:\\Users\\panyi\\Pictures\\20201204110839.png", cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (500, 500))
mask = img.copy()

# 二值化，100为阈值，小于100的变为255，大于100的变为0
# 也可以根据自己的要求，改变参数：
# cv2.THRESH_BINARY
# cv2.THRESH_BINARY_INV
# cv2.THRESH_TRUNC
# cv2.THRESH_TOZERO_INV
# cv2.THRESH_TOZERO
_, binaryzation = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY_INV)

# 找到所有的轮廓
contours, _ = cv2.findContours(binaryzation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

area = []

# 找到最大的轮廓
for k in range(len(contours)):
    area.append(cv2.contourArea(contours[k]))
max_idx = np.argmax(np.array(area))

# 填充最大的轮廓
mask = cv2.drawContours(mask, contours, max_idx, 0, cv2.FILLED)

# 保存填充后的图像
cv2.namedWindow("Mask", 0)
cv2.imshow("Mask", mask)
cv2.waitKey(0)
