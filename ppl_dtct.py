import cv2
import numpy as np

cam = cv2.VideoCapture("vid_1.wmv")
template = cv2.imread('temp_1.jpg',0)
w,h = template.shape[::-1]

while True:
    ret, img_rgb = cam.read()
    #img_rgb = cv2.imread(img)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold =0.8
    loc = np.where(res>=threshold)

    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb,pt,(pt[0]+w,pt[1]+h),(0,255,255),2)

    cv2.imshow('Detected',img_rgb)
    cv2.waitKey(5)
    if(cv2.waitKey(1) == ord('q')):
        break
cam.release()
cv2.destroyAllWindows()
