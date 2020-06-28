import face_recognition
import cv2
import numpy as np
import sys
from face_data import get_face_dncodings,get_name#人脸库

# 打开摄像头
video_capture = cv2.VideoCapture(0)

# 导入人脸数据
known_face_encodings = get_face_dncodings()
known_face_names = get_name()

# 初始化一些变量
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

# 开始循环检测
while True:
    # 抓取面部帧调小尺寸并转码bgr->rgb
    ret, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]

    # 开始检测
    if process_this_frame:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # 检测人脸编码是否匹配，容忍度设置为0.4
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance = 0.4)
            name = "Unknown"

            # 使用人脸实时识别
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame
    #print(face_names)
    # 现实结果
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

    # 按q退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        sys.exit()

# 释放摄像头
video_capture.release()
cv2.destroyAllWindows()