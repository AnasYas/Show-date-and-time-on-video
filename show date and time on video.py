import cv2
import datetime
cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
while (cap.isOpened()):
    ret,frame=cap.read()
    if ret ==True:
        font=cv2.FONT_HERSHEY_SIMPLEX
        text='Width:'+str(cap.get(3)),'Height:'+str(cap.get(4))
        datet=str(datetime.datetime.now())
        frame=cv2.putText(frame, text, (10, 50) ,font, 1, (0, 255, 255), 2)
        frame=cv2.putText(frame,datet,(10,100),font,1,(0,255,255),2)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1)==ord(q):
            break
    else:
        break
cap.release()
cv2.waitKey(0)
cv2.destroyAllWindows()
