import cv2
import numpy as np

img = cv2.imread('src/images/space_debris_sample.jpg', 0)

blurred_img = cv2.GaussianBlur(img, (5, 5), 0)

edges = cv2.Canny(img, 100, 200)

cv2.imwrite('src/images/edges_output.jpg', edges)

cv2.imshow('Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()