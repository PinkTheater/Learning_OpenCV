import numpy as np
import cv2

bw = cv2.imread("detect_blob.png", 0)
                                 # ↑ 0: loaded as black and white image
height, width = bw.shape[0:2]
cv2.imshow("Original bw", bw)

""" Homemade Threshold """

binary = np.zeros([height, width, 1], 'uint8')
thresh = 85

for row in range(0, height):
    for col in range(0, width):
        if bw[row, col] > thresh:
            binary[row, col] = 255
        else:
            binary[row, col] = 0

cv2.imshow("Binary bw", binary)

""" opencv Threshold """

ret, thresh = cv2.threshold(bw,thresh,255,cv2.THRESH_BINARY)
cv2.imshow("CV Threshold", thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()