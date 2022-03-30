import cv2
img = cv2.imread('bb/cars_highway.jpg')
target_img = img.copy() # original img

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, otsu = cv2.threshold(gray,-1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
contours, hierarchy = cv2.findContours(otsu, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE) 

COLOR = (0,200,0) # green

for cnt in contours:
    x, y, width, height = cv2.boundingRect(cnt)
    cv2.rectangle(target_img,(x,y),(x+width,y+height),COLOR,2) 


cv2.imshow('BB',target_img)

cv2.waitKey(0)
cv2.destroyAllWindows()