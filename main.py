from webbrowser import BackgroundBrowser
import cv2 as cv
import numpy as np

img = np.zeros((600, 900, 3), dtype= np.uint8)

# background
cv.rectangle(img, (0,0), (900,500), (255,255,85), -1)
cv.rectangle(img, (0,500), (900,600), (75,180,70), -1)

# sun
cv.circle(img, (200,150), 60, (0,255,255), -1)
cv.circle(img, (200,150), 75, (220,255,255), 10)

# **tree1**
# tree stem
cv.line(img, (600,500), (600,420), (30,65,155), 25)

# tree leafs
triangle1 = np.array([[500,440],[700,440],[600,75]], dtype= np.int32)
cv.fillPoly(img, [triangle1], (75,180,70))

# **tree2**
# tree stem
cv.line(img, (710,500), (710,420), (30,65,155), 25)

# tree leafs
triangle2 = np.array([[640,460],[780,460],[710,200]], dtype= np.int32)
cv.fillPoly(img, [triangle2], (75,200,70))

#text
font = cv.FONT_HERSHEY_SCRIPT_SIMPLEX
cv.putText(img, "~AkD Developers~", (100,460), font, 1.5, (255,255,255), 2)

cv.imshow("AkD", img)
cv.waitKey(0)
cv.destroyAllWindows()

