import urllib
from urllib import request, parse
import base64
import json


# client_id 为官网获取的AK， client_secret 为官网获取的SK
def get_token():
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=sr2mtrRCEAQd6Gw0YpPnv5Or&client_secret=c3spw3XQyIWaYfRM9916tqGzhfPsp7gd'
    request = urllib.request.Request(host)
    request.add_header('Content-Type', 'application/json; charset=UTF-8')
    response = urllib.request.urlopen(request)
    content = response.read()
    # 把字符转换为字节
    content = bytes.decode(content)
    # 把字节存入字典中  eval功能：将字符串str当成有效的表达式来求值并返回计算结果
    content = eval(content[:-1])
    return content['access_token']


def img_data(img1Path, img2Path):
    # 把图片转换成base64编码
    f = open(r'%s' % img1Path, 'rb')
    pic1 = base64.b64encode(f.read())
    f.close()
    f = open(r'%s' % img2Path, 'rb')
    pic2 = base64.b64encode(f.read())
    f.close()
    # 将文件转化为可提交信息
    params = json.dumps(
        [{"image": str(pic1, 'utf-8'), "image_type": "BASE64", "face_type": "LIVE", "quality_control": "LOW"},
         {"image": str(pic2, 'utf-8'), "image_type": "BASE64", "face_type": "LIVE", "quality_control": "LOW"}]
    )
    return params.encode(encoding='UTF8')


def faceTest(img1Path, img2Path):
    token = get_token()
    params = img_data(img1Path, img2Path)
    request_url = 'https://aip.baidubce.com/rest/2.0/face/v3/match'
    access_token = get_token()

    # 对比照片
    request_url = request_url + "?access_token=" + access_token
    request = urllib.request.Request(url=request_url, data=params)
    request.add_header('Content-Type', 'application/json')
    response = urllib.request.urlopen(request)
    content = response.read()
    # 评分
    content = eval(content)
    score = content['result']['score']
    if score > 80:
        return "照片相似度为：" + str(score) + "识别成功"
    else:
        return "照片相似度为：" + str(score) + "未识别"


if __name__ == '__main__':
    img1Path = '/Users/vy/PycharmProjects/py3.7/face/data_persion/郑武杰.jpg'
    img2Path = '/Users/vy/PycharmProjects/py3.7/face/unknown_persion/1.jpg'
    print(faceTest(img1Path, img2Path))