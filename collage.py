import cv2 , numpy as np

kg = cv2.imread('D:\\SUMMER PROGRAM\\tasks\\task4\\img1-collage.jpg')
gojo = cv2.imread('D:\\SUMMER PROGRAM\\tasks\\task4\\img2-collage.jpg')

cv2.imshow('img1',kg)
cv2.waitKey()

cv2.imshow('img1',gojo)
cv2.waitKey()

gojo_renew = cv2.resize(gojo,(kg.shape[1],kg.shape[0]))

collage1 = np.hstack([kg,gojo_renew])
cv2.imshow('img1',collage1)
cv2.waitKey()

collage2 = np.vstack([kg,gojo_renew])
cv2.imshow('img1',collage2)
cv2.waitKey()
