import cv2
print ("Package Imported")

img = cv2.imread("SourceFile/gintama.jpeg")

cv2.imshow("output",img)
cv2.waitKey(0)