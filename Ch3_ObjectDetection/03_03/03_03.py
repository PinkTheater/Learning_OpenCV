import numpy as np
import cv2

img = cv2.imread("sudoku.png", 0)
cv2.imshow("Origin", img)

ret, thresh = cv2.threshold(img, 85, 255, cv2.THRESH_BINARY)
cv2.imshow("Thresh", thresh)

thresh_adapt = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
cv2.imshow("Adaptive Thresh", thresh_adapt)

cv2.waitKey(0)
cv2.destroyAllWindows()