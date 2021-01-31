import numpy as np
import cv2

image = cv2.imread("thresh.jpg")
cv2.imshow("Original", image)

""" Demonstrate the effect of GaussianBlur """
blur = cv2.GaussianBlur(image, (5,55), 0)
cv2.imshow("Blur", blur)

""" Demonstrate the effects of Dilation and Erosion """
kernel = np.ones((5,5), 'uint8')
dilate = cv2.dilate(image,kernel,iterations=1)
erode = cv2.erode(image,kernel,iterations=1)
cv2.imshow("Dilation",dilate)
cv2.imshow("Erosion",erode)


cv2.waitKey(0)
cv2.destroyAllWindows()