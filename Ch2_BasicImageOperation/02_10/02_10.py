import numpy as np
import cv2

color = (0,255,0)
radius = 10
pressed = False

# Global variables
canvas = np.ones([500,500,3],'uint8')*255

# click callback
def click(event, x, y, flags, param):
	global canvas, pressed
        
	if event == cv2.EVENT_LBUTTONDOWN:
		pressed = True
		cv2.circle(canvas, (x,y), radius, color, -1)
	elif event == cv2.EVENT_MOUSEMOVE and pressed == True:
		cv2.circle(canvas, (x,y), radius, color, -1)
	elif event == cv2.EVENT_LBUTTONUP:
		pressed = False

# window initialization and callback assignment
cv2.namedWindow("canvas")
cv2.setMouseCallback("canvas", click)

# Forever draw loop
while True:

    cv2.imshow("canvas",canvas)

    ch = cv2.waitKey(1000)
    if ch & 0xFF == ord('q'):
        break
    elif ch & 0xFF == ord('b'):
        color = (255,0,0)
        print(color)
    elif ch & 0xFF == ord('g'):
        color = (0,255,0)	
        print(color)
    else:
        print(ch)

cv2.destroyAllWindows()