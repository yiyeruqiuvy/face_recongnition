import face_recognition
import cv2
import sys
from face_data import get_name_id
from face_search import get_persion

# 打开摄像头
video_capture = cv2.VideoCapture(0)

# 初始化一些变量
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

# 开始循环检测
while True:
    # 抓取面部帧调小尺寸1/4并转码bgr->rgb
    ret, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]

    # 开始检测
    if process_this_frame:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # 使用云端检测
            i = 0

            '''k = cv2.waitKey(1)
            if k == ord('s'):
                cv2.imwrite('/Users/vy/PycharmProjects/py3.7/face/img/' + str(i) + '.jpg', frame)
                print("截图成功")
                name_id = get_persion('/Users/vy/PycharmProjects/py3.7/face/img/' + str(i) + '.jpg')
                name = get_name_id(name_id)
                face_names.append(name)
                i += 1'''

            cv2.imwrite('/Users/vy/PycharmProjects/py3.7/face/img/' + str(i) + '.jpg', frame)
            #print("截图成功")
            name_id = get_persion('/Users/vy/PycharmProjects/py3.7/face/img/' + str(i) + '.jpg')
            name = get_name_id(name_id)
            face_names.append(name)
            i += 1
    process_this_frame = not process_this_frame

    # 显示结果
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4
        # 添加人脸框
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        # 添加名字，只能显示中文
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
    # 显示结果
    cv2.imshow('Video', frame)
    #time.sleep(2)
    print("识别成功")
    # 按q退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        sys.exit()

# 释放摄像头
video_capture.release()
cv2.destroyAllWindows()