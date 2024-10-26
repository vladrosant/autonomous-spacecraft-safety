import cv2
import numpy as np

img = cv2.imread('images/space_debris_sample.jpg', 0)

edges = cv2.Canny(img, 100, 200)

cv2.imwrite('edges_output.jpg', edges)

cv2.imshow('Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()