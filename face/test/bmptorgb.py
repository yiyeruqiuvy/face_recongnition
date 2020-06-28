# coding:utf-8
import os
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

#删除.jpg文件
def del_files(path):
    for root , dirs, files in os.walk(path):
        for name in files:
            if name.endswith(".bmp"):   #指定要删除的格式，这里是jpg 可以换成其他格式
                os.remove(os.path.join(root, name))
                print ("Delete File: " + os.path.join(root, name))

file_path = "/Users/vy/PycharmProjects/py3.7/face/y"
bmpToJpg_grayToRGB(file_path)
del_files(file_path)