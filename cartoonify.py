import cv2
import numpy as np

img = cv2.imread("이미지 경로")

data = np.float32(img).reshape((-1, 3))
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 0.001)

K = 10
ret, label, center = cv2.kmeans(data, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

center = np.uint8(center)
color = center[label.flatten()]
color = color.reshape(img.shape)

color = cv2.bilateralFilter(color, 9, 50, 50)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5) 
blur = cv2.GaussianBlur(gray, (21, 21), 0)
pencil_sketch = cv2.divide(gray, blur, scale=256.0)
_, ink_sketch = cv2.threshold(pencil_sketch, 245, 255, cv2.THRESH_BINARY)

kernel_close = np.ones((1, 1), np.uint8)
ink_sketch = cv2.morphologyEx(ink_sketch, cv2.MORPH_CLOSE, kernel_close)

kernel_erode = np.ones((1, 1), np.uint8)
ink_sketch = cv2.erode(ink_sketch, kernel_erode, iterations=1)
cartoon = cv2.bitwise_and(color, color, mask=ink_sketch)
merge = np.hstack((img, cartoon))


cv2.imshow("The Ultimate Cartoon Rendering", merge)
cv2.waitKey(0)
cv2.destroyAllWindows()