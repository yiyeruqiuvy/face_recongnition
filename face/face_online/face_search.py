# encoding:utf-8
import urllib
from urllib import request, parse
import requests
import base64
from urllib.parse import urlencode

'''
人脸搜索
'''
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

def get_persion(url):
    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/search"
    with open(url, 'rb') as image:  # 转base64编码
        img = base64.b64encode(image.read())
        params = {'image': '' + str(img, 'utf-8') + '', 'image_type': 'BASE64', 'group_id_list': 'group_repeat,group_233', 'quality_control':'LOW', 'liveness_control':'NORMAL', 'group_id_list':'group_1'}
        # 对base64数据进行urlencode解析，返回值为字符串
        params = urlencode(params)
        #params = "{\"image\":\"str(img, 'utf-8')\",\"image_type\":\"FACE_TOKEN\",\"group_id_list\":\"group_repeat,group_233\",\"quality_control\":\"LOW\",\"liveness_control\":\"NORMAL\"
    access_token = get_token()
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/json'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        res = response.json()
        if res['error_msg'] == 'SUCCESS':
            name_id = res['result']['user_list'][0]['user_id']
            return name_id
        else:
            return '404'
get_persion("/Users/vy/PycharmProjects/py3.7/face/img/0.jpg")