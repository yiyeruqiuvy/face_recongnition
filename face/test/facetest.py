# encoding:utf-8
import urllib
from urllib import request, parse
import requests


'''
获取用户人脸列表
'''
#获取access_token
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

#获取人脸数据
def get_face():
    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/faceset/face/getlist"
    params = "{\"user_id\":\"2017213083\",\"group_id\":\"group_1\"}"
    access_token = get_token()
    print(access_token)
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/json'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        print (response.json())

if __name__ == '__main__':
    get_face()
