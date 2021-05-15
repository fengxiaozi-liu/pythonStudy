"""
csv文件：
    定义：
        Comma-Separated Values，中文叫逗号分隔值或者是字符分隔值，其文件以纯文本的形式存储表格数据。
        可以把它3理解为一个表格，只不过这个表格是以纯文本的形式显示的，单元格与单元格之间，默认使用逗号
        进行分隔，每行数据使用换行进行分隔
    语法：
        写入文件：
            import csv
            file_name = open('文件路径', mode = 'w',encoding)
            创建一个写入对象x = csv.writer(file_name)
            x.writerow = ([数据])
            file_name.close()
        读取文件：
            file_name = open('文件路径', mode = 'r',encoding,newline='')
            创建一个读取对象x = csv.reader(file_name)
            for data in x:
                print(data)
            file_name.close()


"""
import csv

# 文件的写入
file = open('文档.csv', 'w', encoding='utf8')
w = csv.writer(file)
w.writerow(['name', 'age', 'score', 'city'])
w.writerow(['zhangsan', 18, 98, '香格里拉'])
# 文件的读取
file1 = open('info.csv', 'r')
# print(file1.read().decode('gbk'))
x = csv.reader(file1)
for data in x:
    print(data[0])
file.close()
file1.close()
