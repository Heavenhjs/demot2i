'''
作者：胡劲松
日期：2022年08月01日
'''
import os  #导入os库
import urllib  #导入urllib库
import urllib.request

def file_downloand():  #######文件下载
    if os.path.exists("文件路径") == False:  # 判断是否存在文件

        # 文件url
        image_url = 'https://drive.google.com/file/d/1KbaNkJK7zPqjy1OGyOaLuGLOyJd6JRRD/view?usp=sharing'

        # 文件基准路径
        basedir = os.path.abspath(os.path.dirname(__file__))
        # 下载到服务器的地址
        file_path = os.path.join(basedir, 'data')

        try:
            # 如果没有这个path则直接创建
            if not os.path.exists(file_path):
                os.makedirs(file_path)
            file_suffix = os.path.splitext(image_url)[1]
            filename = '{}{}'.format(file_path, file_suffix)  # 拼接文件名。
            urllib.request.urlretrieve(image_url, filename=filename)
            print("成功下载文件")
        except IOError as exception_first:  #设置抛出异常
            print(1, exception_first)

        except Exception as exception_second:  #设置抛出异常
            print(2, exception_second)
    else:
        print("文件已经存在！")

file_downloand()
