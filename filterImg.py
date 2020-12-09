import cv2

img  = cv2.imread("SourceFile/gintama1.jpg")

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgAladin = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny = cv2.Canny(img,60,0)

cv2.imshow("Gray Image", imgGray)
cv2.imshow("Aladin Image", imgAladin)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
print(img.shape)
cv2.waitKey(0)