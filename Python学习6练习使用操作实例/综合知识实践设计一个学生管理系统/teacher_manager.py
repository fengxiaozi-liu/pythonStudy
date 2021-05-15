"""
创建一个老师类
属性：姓名 登录密码
行为：
    能够增加学生
    能够查看学生
    能够删除学生
    能够修改学生的信息
"""
import students_manager
import file_manager


class Teacher:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.student_list = []
        self.teacher_list = []
        self.teacher_dict = {}
        file_manager.write_pickle(self.student_list, '学生信息.txt')

    def add_student(self):
        s = students_manager.create_student()
        student_list = file_manager.read_pickle('学生信息.txt')
        student_list.append(s)
        file_manager.write_pickle(student_list, '学生信息.txt')

    def watch_all_student(self):
        student_list = file_manager.read_pickle('学生信息.txt')
        if len(student_list) == 0:
            print('当前这个老师下还没有学生')
        for each_student in student_list:
            print(
                f'学号：{each_student.student_id}, 姓名：{each_student.name}，年龄：{each_student.age}, 性别：{each_student.gender}, '
                f'电话：{each_student.tel}')

    def find_student_name(self):
        count = 0
        s = None
        student_list = file_manager.read_pickle('学生信息.txt')
        while True:
            student_name = input('请输入你想要查看的学生信息的姓名 ')
            if isinstance(student_name, str):
                break
            else:
                print('请输入正确的名字')
        for each in student_list:
            if each.name == student_name:
                count += 1
                s = each
        if count == 1:
            print(f'学号：{s.student_id}, 姓名：{s.name}, 年龄：{s.age},, 性别：{s.gender},, 电话：{s.tel}')
        else:
            print('您输入的名字不存在请仔细核对信息')

    def find_student_id(self):
        count = 0
        s = None
        student_list = file_manager.read_pickle('学生信息.txt')
        while True:
            student_id = int(input('请输入您想要查看的学生的id '))
            if isinstance(student_id, int):
                break
            else:
                print('请输入正确的id')
        for each in student_list:
            if each.student_id == student_id:
                count += 1
                s = each
        if count == 1:
            print(f'学号：{s.student_id}, 姓名：{s.name}, 年龄：{s.age},, 性别：{s.gender},, 电话：{s.tel}')
        else:
            print('您输入的名字不存在请仔细核对信息')

    def modify_student(self):
        s = None
        student_list = file_manager.read_pickle('学生信息.txt')
        while True:
            student_name = input('请输入你想要修改的学生的姓名 ')
            if isinstance(student_name, str):
                break
            else:
                print('请输入一个学生的姓名')
        for each in student_list:
            if each.name == student_name:
                s = each
        print(s)
        information = input('请输入你想要修改的内容 学号？ 姓名？ 年龄？ 性别？ 电话？')
        if information == '学号':
            student_id = int(input('你想要将学号修改为 '))
            s.student_id = student_id
        elif information == '姓名':
            name = input('你想要将姓名修改为 ')
            s.name = name
        elif information == '年龄':
            age = int(input('你想要将年龄修改为 '))
            s.age = age
        elif information == '性别':
            gender = input('你想要将性别修改为 ')
            s.gender = gender
        elif information == '电话':
            tel = int(input('你想要将电话修改为 '))
            s.tel = tel
        else:
            print('请按照提示输入')
        file_manager.write_pickle(student_list, '学生信息.txt')

    def del_student(self):
        student_list = file_manager.read_pickle('学生信息.txt')
        while True:
            student_name = input('请输入你想要删除的学生的姓名 ')
            if isinstance(student_name, str):
                break
            else:
                print('请输入一个学生的姓名')
        for each in student_list:
            if each.name == student_name:
                student_index = student_list.index(each)
                student_list.pop(student_index)


def register():
    while True:
        users = input('请输入一个3~6位的用户名 ')
        if 3 <= len(users) <= 6:
            user = users
            break
    while True:
        passwords = input('请输入一个6~12位的密码 ')
        if 6 <= len(passwords) <= 12:
            password = passwords
            break
    teacher = Teacher(user, password)
    teacher.teacher_list.append(teacher)
    teacher.teacher_dict[user] = password
    file_manager.write_json(teacher.teacher_dict, '老师信息.txt')
    file_manager.write_pickle(teacher.teacher_list, '老师对象.txt')


def login():
    teacher_list = file_manager.read_pickle('老师对象.txt')
    teacher_user = input('请输入你的用户名 ')
    count = 0
    for each in teacher_list:
        if each.name == teacher_user:
            count += 1
            num = teacher_list.index(each)
    if count == 1:
        i = 0
        while i < 3:
            teacher_password = input('请输入密码 ')
            if teacher_list[num].password == teacher_password:
                return teacher_list[num]
            else:
                print('密码不正确')
            i += 1
        if i == 3:
            print('你的密码输入次数用完了, 好好想想明天再来吧')

    else:
        print('您要找的用户名不存在，请仔细核对信息')

