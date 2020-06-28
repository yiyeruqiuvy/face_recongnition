import cv2
import sys

cap = cv2.VideoCapture(0)
i = 0
while (1):
    ret, frame = cap.read()
    k = cv2.waitKey(1)
    if k == ord('q'):
        sys.exit()
    elif k == ord('s'):
        cv2.imwrite('/Users/vy/PycharmProjects/py3.7/face/img/' + str(i) + '.jpg', frame)
        i += 1
        print("截图成功")
    cv2.imshow("capture", frame)
cap.release()
