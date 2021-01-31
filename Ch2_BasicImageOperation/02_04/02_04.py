import numpy as np
import cv2

color = cv2.imread("butterfly.jpg", 1)
#cv2.imshow("Image", color)
#cv2.moveWindow("Image",0,0)
print(color.shape)
height, width, channels = color.shape

b,g,r = cv2.split(color)

rgb_split = np.empty([height, width*3, 3], 'uint8')
rgb_split[:, 0:width] = cv2.merge([b,b,b])
rgb_split[:, width:width*2] = cv2.merge([g,g,g])
rgb_split[:, width*2:width*3] = cv2.merge([r,r,r])
#rgb_split = np.concatenate((b,g,r), axis = 1)

print(rgb_split.shape)

#cv2.imshow("Blue", rgb_split[:, 0:width])
#cv2.imshow("Green", rgb_split[:, width:width*2])
#cv2.imshow("Red", rgb_split[:, width*2:width*3])

cv2.imshow("Channels",rgb_split)
cv2.moveWindow("Channels",0,height)

hsv = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(hsv)
hsv_split = np.concatenate((h,s,v), axis = 1)
cv2.imshow("ChannelHSV",hsv_split)
print(hsv_split.shape)

cv2.waitKey(0)
cv2.destroyAllWindow()
