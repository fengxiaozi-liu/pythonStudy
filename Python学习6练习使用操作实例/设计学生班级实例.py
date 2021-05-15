"""
学生类：
    属性： 学号 姓名 年龄 成绩
班级类：
    属性： 班级名称 班级中的学生
    方法：查看班级中所有学生的信息
         查看指定学号的信息
         查看班级中成绩不及格的信息
         将班级中的学生按照降序排序
"""
import sys


class Students:
    """
    这是一个学生类 里面含有一个学生的姓名 学号 年龄 成绩的信息
    """

    def __init__(self, name, id, age, score):
        self.name = name
        self.id = id
        self.age = age
        self.score = score

    def __str__(self):
        return f'{[self.id, self.name, self.age, self.score]}'


class Grade:
    """
    这是一个班级类 有班级名称 班级中的学生
    可以查看班级每个学生的基本信息
    可以查看指定学号的学生信息
    可以查看成绩不及格学生的学生信息
    可以按照成绩对学生进行排序
    """

    def __init__(self, name):
        self.name = name
        self.students = []

    def __str__(self):
        return f'{self.name},学生有{len(self.students)}个'

    def add_student(self, s):
        """
        这是一个增加班级学生的方法
        :param s: 可以是一个学生 也可以是多个学生组成的列表
        :return: 班级中全部学生的列表
        """
        self.students.extend(s)
        return self.students

    def show_students(self):
        """
        展示所有学生信息的方法
        :return: 每一个学生的基本信息
        """
        for each in self.students:
            print(each)
        print('-' * 30)

    def find_student(self):
        """
        根据学生的id查找学生的基本信息
        :return:
        """
        count = 0
        p = None
        content = sys.stdin
        student_id = int(content.readline().rstrip('\n'))
        for each in self.students:
            if each.id == student_id:
                count += 1
                p = each
        if count == 1:
            return p
        else:
            return f'您要查找的学生id{student_id}不存在，请仔细核对信息'

    def find_unqualified(self):
        """
        筛选出成绩不合格学生的方法
        """
        unqualified = filter(lambda a: a.score < 60, self.students)
        for each in unqualified:
            print(each)
        print('-' * 30)

    def sort_students(self):
        """
        按照学生的信息对学生进行降序排序
        :return:
        """
        for i in range(len(self.students)):
            for j in range(i):
                if self.students[j].score < self.students[j + 1].score:
                    self.students[j], self.students[j + 1] = self.students[j + 1], self.students[j]
        for each in self.students:
            print(each)
        print('-' * 30)


# 创建四个学生
s1 = Students('张三', 123, 8, 92)
s2 = Students('李四', 456, 9, 59)
s3 = Students('王五', 789, 7, 61)
s4 = Students('jack', 147, 10, 48)
# 创建一个班级
c1 = Grade('五年级三班')
# 将学生放到班级里
c1.add_student([s1, s2, s3, s4])
# 查看班级的所有信息
c1.show_students()
# 查找成绩不合格的学生
c1.find_unqualified()
# 按成绩对学生进行排名
c1.sort_students()
# 查找指定学号的学生
print(c1.find_student())
print('完成所有操作了，结束')
