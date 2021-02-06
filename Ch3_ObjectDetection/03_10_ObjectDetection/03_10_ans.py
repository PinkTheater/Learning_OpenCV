import numpy as np
import cv2
import random

img = cv2.imread("fuzzy.png",1)
cv2.imshow("Original", img)

# original image ⇒ gray ⇒ blur ⇒　binary
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
blur = cv2.GaussianBlur(gray, (5,5), 0)
binary = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 205, 1)
cv2.imshow("Step 1. Gray", gray)
cv2.imshow("Step 2. Blur", blur)
cv2.imshow("Step 3. Binary", binary)


# Find Contours
contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


# Draw
index = -1
thickness = -1    ### -1 to fill

canvas = np.zeros([img.shape[0], img.shape[1], 3], 'uint8')

''' method 1 '''
print("Number of contours from cv2.findContours: ", len(contours))

filtered = []
for c in contours:
    if cv2.contourArea(c) < 1000: continue
    filtered.append(c)

print("Number of contours with area larger than 1000: ", len(filtered))

for f in filtered:
    print("Area: {}, Perimeter: {}".format(cv2.contourArea(f), cv2.arcLength(f, True)))
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    cv2.drawContours(canvas, [f], index, color, thickness)

''' method 2
for c in contours:
    area = cv2.contourArea(c)
    
    if area > 1000:
        perimeter = cv2.arcLength(c, True)
        print("Area: {}, Perimeter: {}".format(area, perimeter))
        cv2.drawContours(canvas, [c], index, color, thickness)
'''

cv2.imshow("Step 4. Modified Image", canvas)


cv2.waitKey(0)
cv2.destroyAllWindows()