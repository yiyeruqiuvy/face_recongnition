import face_recognition

# 添加人脸库
ranhongfei_image = face_recognition.load_image_file("/Users/vy/PycharmProjects/py3.7/face/data_persion/冉翃飞.jpg")
ranhongfei_face_encoding = face_recognition.face_encodings(ranhongfei_image)[0]

wanghang_image = face_recognition.load_image_file("/Users/vy/PycharmProjects/py3.7/face/data_persion/王航.jpg")
wanghang_face_encoding = face_recognition.face_encodings(wanghang_image)[0]

peiqianfeng_image = face_recognition.load_image_file("/Users/vy/PycharmProjects/py3.7/face/data_persion/裴乾锋.jpg")
peiqianfeng_face_encoding = face_recognition.face_encodings(peiqianfeng_image)[0]

fuaihua_image = face_recognition.load_image_file("/Users/vy/PycharmProjects/py3.7/face/data_persion/傅爱华.jpg")
fuaihua_face_encoding = face_recognition.face_encodings(fuaihua_image)[0]

daixinzhu_image = face_recognition.load_image_file("/Users/vy/PycharmProjects/py3.7/face/data_persion/戴欣祝.jpg")
daixinzhu_face_encoding = face_recognition.face_encodings(daixinzhu_image)[0]

longhang_image = face_recognition.load_image_file("/Users/vy/PycharmProjects/py3.7/face/data_persion/龙杭.jpg")
longhang_face_encoding = face_recognition.face_encodings(longhang_image)[0]

wenruoyu_image = face_recognition.load_image_file("/Users/vy/PycharmProjects/py3.7/face/data_persion/文若愚.jpg")
wenruoyu_face_encoding = face_recognition.face_encodings(wenruoyu_image)[0]

jianjinchi_image = face_recognition.load_image_file("/Users/vy/PycharmProjects/py3.7/face/data_persion/蹇金池.jpg")
jianjinchi_face_encoding = face_recognition.face_encodings(jianjinchi_image)[0]

lidongjun_image = face_recognition.load_image_file("/Users/vy/PycharmProjects/py3.7/face/data_persion/李东俊.jpg")
lidongjun_face_encoding = face_recognition.face_encodings(lidongjun_image)[0]


# 创建已知面部编码及其名称的数组
def get_face_dncodings():
    known_face_encodings = [
        ranhongfei_face_encoding,
        peiqianfeng_face_encoding,
        longhang_face_encoding,
        daixinzhu_face_encoding,
        lidongjun_face_encoding,
        fuaihua_face_encoding,
        jianjinchi_face_encoding,
        wanghang_face_encoding
    ]
    return known_face_encodings

def get_name():
    known_face_names = [
        "ranhongfei",
        "peiqianfeng",
        "longhang",
        "daixinzhu",
        "lidongjun",
        "fuaihua",
        "jianjinchi",
        "wanghang"
    ]
    return known_face_names

def get_name_id(id):
    if id == '2017213083':
        return 'ranhongfei'
    elif id == '2017213084':
        return 'peiqianfeng'
    elif id == '2017213085':
        return 'longhang'
    elif id == '2017213086':
        return 'daixinzhu'
    elif id == '2017213087':
        return 'lidongjun'
    elif id == '2017213088':
        return 'fuaihua'
    elif id == '2017213089':
        return 'jianjinchi'
    elif id == '2017213090':
        return 'wanghang'
    elif id == '2017213091':
        return 'wenruoyu'
    elif id == '404':
        return "do not known"

