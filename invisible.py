import cv2
import numpy

cap=cv2.VideoCapture(0)
back=cv2.imread('./image.jpg')
while cap.isOpened():
    ret,frame=cap.read()
    if ret:
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        #cv2.imshow("hsv",hsv)
        #lower: hue-10,100,100 , higher:hue+10,255,255
        blue=numpy.uint8([[[0,0,255]]])
        hsv_blue=cv2.cvtColor(blue,cv2.COLOR_BGR2HSV)
        #print(hsv_blue)

        l_blue=numpy.array([0,100,100])
        u_blue=numpy.array([10, 255 ,255])
        mask=cv2.inRange(hsv,l_blue,u_blue)
        #cv2.imshow("mask",mask)
        demo1=cv2.bitwise_and(back,back,mask=mask)
        mask=cv2.bitwise_not(mask)
        demo2=cv2.bitwise_and(frame,frame,mask=mask)
        cv2.imshow("cloak",demo1+demo2)
        if cv2.waitKey(5)==ord('q'):
            break
cap.release()
cv2.destroyAllWindows()
