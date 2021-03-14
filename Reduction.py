import argparse
import imutils
import cv2
import matplotlib.pyplot as plt
import numpy as np

# 读取图片文件
img = cv2.imread('C:\\Users\\panyi\\Pictures\\Capture\\example1.jpg')

# 调整视频尺寸
img = imutils.resize(img, width=500)

# 转换成RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Plot the image with different kernel sizes
fig, axs = plt.subplots(nrows=1, ncols=3, figsize=(10, 5))

for ind, s in enumerate([5, 11, 17]):
    img_blurred = cv2.blur(img, ksize=(s, s))
    ax = axs[ind]
    ax.imshow(img_blurred)
    ax.axis('off')
plt.show()
