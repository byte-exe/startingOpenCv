import cv2
import numpy as np
img = cv2.imread('SourceFile/gintama1.jpg')


imgHor = np.hstack((img,img))
imgVer = np.vstack((img,img))

cv2.imshow("Horizontal", imgHor)
cv2.imshow("Vertikal", imgVer)



cv2.waitKey(0)