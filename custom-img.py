import cv2
import numpy as np

car = np.zeros((512,512,3))

car[:,:] = [0,255,255]

top = cv2.circle(car,(200,240),50, (0,255,0), -1)
top = cv2.circle(car,(200,240),50, (0,0,0), 4)
body = cv2.rectangle(car,(130,260),(382,382),(0,0,245),-1)
body = cv2.rectangle(car,(130,260),(382,382),(0,0,0),3)
tyre1 = cv2.circle(car,(130,382),40, (0,0,0), 4)
tyre1 = cv2.circle(car,(130,382),40, (255,255,255), -1)
tyre1 = cv2.circle(car,(130,382),20, (0,0,0), 4)
tyre2 = cv2.circle(car,(382,382),40, (0,0,0), 4)
tyre2 = cv2.circle(car,(382,382),40, (255,255,255), -1)
tyre2 = cv2.circle(car,(382,382),20, (0,0,0), 4)
road = cv2.line(car,(0,422),(512,422),(0,0,0),10)

cv2.imshow('custom car ',car )
cv2.waitKey()