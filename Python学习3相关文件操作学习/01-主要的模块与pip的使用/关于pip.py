"""
pip: 是Python第三方的工具
    在安装Python的过程中，同时还会安装pip软件，它是Python的包管理工具，可以用来查找，下载，安装和卸载Python的第三方资源包
    应用环境：
        Python中没有但是有人写出来模块，可以用pip下载
    用法：
        打开cmd小黑窗口或者pycharm的Terminal
        输入：
           pip install <package_name> 用来下载第三方模块
           pip uninstall <package_name> 用来卸载第三方软件
           pip list 用来列出当前环境安装的模块名和版本号
           pip freeze 用来列出当前环境安装的模块名和版本号
           {pip freeze > file_name.txt 把环境安装的模块名和版本号重定向输出到指定文件
           pip install -r file_name.txt 读取文件里面的模块名和版本号并安装
        补充：
        如果下载速度比较慢的话可以转到国内下载
        输入：
           国内安装路径
           pip install <package_name> -i https://pypi.douban.com/simple
           临时修改 只修改一个文件的下载路径
           pip install <package_name> -i <url> 从指定的位置下载包
           永久修改 修改全部文件的下载路径
           在当前目录下新建一个pip.ini文件夹
           在文件夹的内部输入
           [global]
           index = <url>
           [install]
           trusted-host=<url>

"""
from flask import Flask
import sys

print(sys.path)
# 得到sys.path 的结果 是文件夹的相关目录，在这些目录下的模块都可以使用
# ['C:\\Users\\19693\\Desktop\\code\\Python学习3相关文件操作学习', 'C:\\Users\\19693\\Desktop\\code',
#  'C:\\Users\\19693\\AppData\\Local\\Programs\\Python\\Python38-32\\python38.zip',
#  'C:\\Users\\19693\\AppData\\Local\\Programs\\Python\\Python38-32\\DLLs',
#  'C:\\Users\\19693\\AppData\\Local\\Programs\\Python\\Python38-32\\lib',
#  'C:\\Users\\19693\\AppData\\Local\\Programs\\Python\\Python38-32',
#  'C:\\Users\\19693\\AppData\\Local\\Programs\\Python\\Python38-32\\lib\\site-packages',
#  'C:\\Users\\19693\\AppData\\Local\\Programs\\Python\\Python38-32\\lib\\site-packages\\win32',
#  'C:\\Users\\19693\\AppData\\Local\\Programs\\Python\\Python38-32\\lib\\site-packages\\win32\\lib',
#  'C:\\Users\\19693\\AppData\\Local\\Programs\\Python\\Python38-32\\lib\\site-packages\\Pythonwin']
