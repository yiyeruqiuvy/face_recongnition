import face_recognition
import os
import re
from PIL import Image

# bmp 转换为jpg，灰度图转RGB
def bmpToJpg_grayToRGB(file_path):
    for fileName in os.listdir(file_path):
        print("转换前图片："+ fileName)
        newFileName = fileName[0:fileName.find(".bmp")]+".jpg"
        print("转换后图片："+ newFileName)
        im = Image.open(file_path+"/"+fileName)
        rgb = im.convert('RGB')      #灰度转RGB
        rgb.save(file_path+"/"+newFileName)
    return newFileName

#删除.jpg文件
def del_files(path):
    for root , dirs, files in os.walk(path):
        for name in files:
            if name.endswith(".bmp"):   #指定要删除的格式
                os.remove(os.path.join(root, name))
                print ("Delete File: " + os.path.join(root, name))

file_path = "/Users/vy/PycharmProjects/py3.7/face/y"
unknowpersion = bmpToJpg_grayToRGB(file_path)
del_files(file_path)

#提取姓名
dir_path = '/Users/vy/PycharmProjects/py3.7/face/data_persion'
nameList = os.listdir(dir_path)
del nameList[0]
j = 0
for i in nameList:
    i = re.sub(r'.jpg', ' ',i)
    nameList[j] = i
    j = j + 1

#读取已知人脸特征
picture_of_1 = face_recognition.load_image_file("/Users/vy/PycharmProjects/py3.7/face/data_persion/郑武杰.jpg")
picture_of_2 = face_recognition.load_image_file("/Users/vy/PycharmProjects/py3.7/face/data_persion/骚猪.jpg")
picture_of_3 = face_recognition.load_image_file("/Users/vy/PycharmProjects/py3.7/face/data_persion/王航.jpg")
picture_of_4 = face_recognition.load_image_file("/Users/vy/PycharmProjects/py3.7/face/data_persion/裴乾锋.jpg")

face_encoding_1 = face_recognition.face_encodings(picture_of_1)[0]
face_encoding_2 = face_recognition.face_encodings(picture_of_2)[0]
face_encoding_3 = face_recognition.face_encodings(picture_of_3)[0]
face_encoding_4 = face_recognition.face_encodings(picture_of_4)[0]
face_encoding = [face_encoding_1, face_encoding_2, face_encoding_3, face_encoding_4]

#读取未知图片特征
unknown_picture = face_recognition.load_image_file("/Users/vy/PycharmProjects/py3.7/face/y/" + unknowpersion)
unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]

#对比结果
results = face_recognition.compare_faces(face_encoding, unknown_face_encoding, tolerance = 0.4)
j = 0
for i in results:
    if i == True:
        print("识别成功："+nameList[j])
    else:
        print("不是"+nameList[j])
    j = j + 1