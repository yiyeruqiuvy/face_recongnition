import face_recognition
picture_of_me = face_recognition.load_image_file("data_persion/骚猪.jpg")
my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]

# my_face_encoding now contains a universal 'encoding' of my facial features that can be compared to any other picture of a face!

unknown_picture = face_recognition.load_image_file("unknown_persion/4.jpg")
unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]

# Now we can see the two face encodings are of the same person with `compare_faces`!

results = face_recognition.compare_faces(unknown_face_encoding, [my_face_encoding], tolerance = 0.3)

if results[0] == True:
    print("同一个人")
else:
    print("It's not a picture of me!")