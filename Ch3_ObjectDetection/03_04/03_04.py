import numpy as np
import cv2

img = cv2.imread('faces.jpeg',1)

# Split into HSV, and output the HSV image
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h = hsv[:,:,0]
s = hsv[:,:,1]
v = hsv[:,:,2]

hsv_split = np.concatenate((h,s,v), axis=1)
hsv_split_smaller = cv2.resize(hsv_split, (0,0), fx=0.2, fy=0.2)
cv2.imshow("Split HSV", hsv_split_smaller)

# hardcore skin detection with filter of hue and saturation
ret, min_sat = cv2.threshold(s, 40, 255, cv2.THRESH_BINARY)
ret, max_hue = cv2.threshold(h, 15, 255, cv2.THRESH_BINARY_INV)
skin_detection = cv2.bitwise_and(min_sat, max_hue)
filters_split = np.concatenate((min_sat, max_hue, skin_detection), axis = 1)
filters_split_smaller = cv2.resize(filters_split, (0,0), fx=0.2, fy=0.2)
cv2.imshow("Skin Detection", filters_split_smaller)

cv2.waitKey(0)
cv2.destroyAllWindows()