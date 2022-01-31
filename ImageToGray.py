import cv2

Original_Img = cv2.imread('Lakshmanaprakash.jpg')
cv2.imshow("Original Image", Original_Img)
Gray_Img = cv2.cvtColor(Original_Img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image", Gray_Img)
cv2.waitKey(0)