import cv2
import os

img = cv2.imread(os.path.join('.', 'dogs.jpg'))

print(img.shape)
cropped_img = img[80:620, 200:800]

cv2.imshow('frame', cropped_img)
cv2.waitKey(0)