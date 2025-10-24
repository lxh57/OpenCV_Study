import os
import cv2

img = cv2.imread(os.path.join('.', 'birds.jpg'))
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# to work with contours, make the objects are white to detect, use BINARY_INV
ret, thresh = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY_INV)

contour, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contour:
    if cv2.contourArea(cnt) > 200:
        #cv2.drawContours(img, [cnt], -1, (0, 255, 0), 1)
        x1,y1,w,h = cv2.boundingRect(cnt)
        cv2.rectangle(img,(x1,y1),(x1+w,y1+h),(0,255,0),2)


cv2.imshow("img", img)
cv2.imshow("img_thresh", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()