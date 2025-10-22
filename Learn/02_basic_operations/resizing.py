import cv2
import os

img = cv2.imread(os.path.join('.', 'dogs.jpg'))
resized_img = cv2.resize(img, (640, 480))

print(img.shape)
print(resized_img.shape)

cv2.imshow('frame', img)
cv2.imshow('resized_img', resized_img)
cv2.waitKey(0)