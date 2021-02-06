################################
### Contour Object Detection ###
################################

import numpy as np
import cv2

# Turn into binary image for convenience of finding contours
img = cv2.imread('detect_blob.png',1)
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
binary = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 161, 1)

    ## show original image and binary one
cv2.imshow("Original Image", img)
cv2.imshow("Binary Image", binary)


# Find Contours
contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


# Draw Contours
imgContours = img.copy()
index = -1   ### -1 to draw all contours ###
thickness = 4
color = (255, 0, 255)

cv2.drawContours(imgContours, contours, index, color, thickness)
cv2.imshow("Image with Contours", imgContours)


cv2.waitKey(0)
cv2.DestroyAllWindows()