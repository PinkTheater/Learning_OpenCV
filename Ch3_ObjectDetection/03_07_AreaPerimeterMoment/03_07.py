###############################
### Area, Perimeter, Center ###
###############################

import numpy as np
import cv2

# Turn into binary image for convenience of finding contours
img = cv2.imread('detect_blob.png',1)
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
cv2.imshow("Binary", thresh)


# Find Contours
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


# Calculate area, perimeter, and center, and then draw it
index = -1
color = (255, 0, 255)
thickness = -1    ### -1 to fill
radius = 4

    ## Create new canvas
objects = np.zeros([img.shape[0], img.shape[1], 3], 'uint8')

    ## Draw contours on canvas and calculate parameters individually
i = 1
for c in contours:
    cv2.drawContours(objects, [c], index, color, thickness)
    
    area = cv2.contourArea(c)
    perimeter = cv2.arcLength(c, True)
    
    M = cv2.moments(c)
    cx = int( M['m10']/M['m00'] )
    cy = int( M['m01']/M['m00'] )
    cv2.circle(objects, (cx, cy), radius, (0, 255, 255), -1)
    
    print("#{} contour - area: {}, perimeter: {}".format(i, area, perimeter))
    i = i + 1

cv2.imshow("Contours", objects)


cv2.waitKey(0)
cv2.destroyAllWindows()