"""
创建一学生类
里面含有学生的基本信息  学号 姓名 年龄 性别 电话
"""


class Students:
    def __init__(self, student_id, name, age, gender, tel):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.gender = gender
        self.tel = tel

    def __str__(self):
        return f'{self.student_id, self.name, self.age, self.gender, self.tel}'


def create_student():
    student_id = int(input('添加学生的id '))
    name = input('添加学生的姓名 ')
    age = int(input('添加学生的年龄 '))
    gender = input('添加学生的性别 ')
    tel = int(input('添加学生的电话 '))
    s = Students(student_id, name, age, gender, tel)
    return s


if __name__ == '__main__':
    create_student()
