import cv2,goku,opm 

#one-punch-man face cropped
opm_face = opm.opm[40:140,400:500]
cv2.imshow('opm face only ',opm_face)
cv2.waitKey() 

#goku face cropped
goku_face = goku.goku[:340,60:520]
cv2.imshow('goku face',goku_face)
cv2.waitKey()

#reshape/resize the cropped part with respect to image it's going to be attached
re_opm_face = cv2.resize(opm_face,(goku_face.shape[1],goku_face.shape[0]))
re_goku_face = cv2.resize(goku_face,(opm_face.shape[1],opm_face.shape[0]))

#swapped face of Goku
opm.opm[40:140,400:500]=re_goku_face
cv2.imshow('opm with goku head ',opm.opm)
cv2.waitKey()

#swapped face of Opm
goku.goku[:340,60:520]=re_opm_face
cv2.imshow('goku with opm head ',goku.goku)
cv2.waitKey()



