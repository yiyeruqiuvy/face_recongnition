import face_recognition

picture_of_1 = face_recognition.load_image_file("data_persion/111.jpg")
my_face_encoding = face_recognition.face_encodings(picture_of_1)
#print(my_face_encoding)
j=0
for i in my_face_encoding:
    print(i)
    print(j)
    j = j+1
unknown_picture = face_recognition.load_image_file("unknown_persion/2.jpg")
unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]

results = face_recognition.compare_faces(my_face_encoding, unknown_face_encoding)

for i in results:
    if i == True:
        print("是同一个人")
    else:
        print("不是同一个人")