
"""
url2picture
"""


import os, time, random,urllib,urllib2

file = open('images.csv')
save_path_val="C:\\image_val\\"

def Image_Download_from_remote(line,save_path): 
    try:
        picurl=line.split(',')[2]
        # 图片地址
        imgData = urllib2.urlopen(picurl).read()
        # 给定图片存放名称
        fileName = save_path + line.split(',')[0] + '.jpg'
        # 文件名是否存在
        if not os.path.exists(fileName):
            output = open(fileName,'wb+')
            output.write(imgData)
            output.close()
    except:
        pass

if __name__=='__main__':
    j = 0
    while 1:
        lines = file.readlines()
        if not lines:
            break
        for line in lines:
            %time Image_Download_from_remote(line,save_path_val)
            j = j + 1
