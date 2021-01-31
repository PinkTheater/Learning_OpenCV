import numpy as np
import cv2

color = cv2.imread("butterfly.jpg",1)

gray = cv2.cvtColor(color,cv2.COLOR_RGB2GRAY)
cv2.imwrite("gray.jpg",gray)

### Three lines shown below seems verbose but actually more efficient than using cv2.split ###
b = color[:,:,0]
g = color[:,:,1]
r = color[:,:,2]

"""
The fourth variable shown in the input of merge is for transparency.
If you input only 3 variables, it will also work without transparency parameter.
"""

rgba = cv2.merge((b,g,r,g))
cv2.imwrite("rgba.png",rgba)