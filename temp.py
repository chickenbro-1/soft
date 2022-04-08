# Sobel边缘检测算子
import os
import cv2
img = cv2.imread('temp.png', 0)#转化为灰度图
x = cv2.Sobel(img, cv2.CV_16S, 1, 0)
y = cv2.Sobel(img, cv2.CV_16S, 0, 1)


print(contours)
cv2.imshow('result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()

