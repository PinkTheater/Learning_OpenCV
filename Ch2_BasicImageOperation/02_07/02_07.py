import numpy as np
import cv2

img = cv2.imread("players.jpg",1)
height, width, channels = img.shape
print("The shape of original image is ", img.shape, ".")

# SCALE
img_half = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
img_StretchVert = cv2.resize(img, (width, int(height*1.5)))
img_StretchVert_near = cv2.resize(img, (width, int(height*1.5)), interpolation=cv2.INTER_NEAREST)

print("The shape of half is ", img_half.shape, ".")
print("The shape of StretchVert is ", img_StretchVert.shape, ".")

cv2.imshow("Half", img_half)
cv2.imshow("StretchVert", img_StretchVert)
cv2.imshow("StretchVert_near", img_StretchVert_near)

# ROTATION
M = cv2.getRotationMatrix2D((width,height), -30, 1)
rotated = cv2.warpAffine(img, M, (width, height))
cv2.imshow("Rotated", rotated)
""" Be careful to the (width, height). There is no minus sign in front 
of height if you want to set rotation origin in the lower right corner. """


cv2.waitKey(0)
cv2.destroyAllWindows()