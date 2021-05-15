import file_manager
import teacher_manager


def start():
    content = file_manager.open_dir('管理系统页面.txt')
    while True:
        operate = input(content+'\n请输入你想要执行的操作')
        if operate == '1':
            teacher = teacher_manager.login()
            student_page = file_manager.open_dir('对学生相关操作页面.txt')
            while teacher != None :
                operate_student = input(student_page+'\n请输入你想要执行的操作')
                if operate_student == '1':
                    teacher.add_student()
                elif operate_student == '2':
                    find_students_page = file_manager.open_dir('查看学生操作页面.txt')
                    while True:
                        find_student = input(find_students_page+'\n请输入你想要执行的操作')
                        if find_student == '1':
                            teacher.watch_all_student()
                        elif find_student == '2':
                            teacher.find_student_name()
                        elif find_student == '3':
                            teacher.find_student_id()
                        elif find_student == '4':
                            break
                        else:
                            print('请执行正确的操作')
                elif operate_student == '3':
                    teacher.del_student()
                elif operate_student == '4':
                    teacher.modify_student()
                elif operate_student == '5':
                    break
                else:
                    print('请执行正确的操作')
        elif operate == '2':
            teacher_manager.register()
        elif operate == '3':
            exit_system = input('请输入0：再看看一会离开, 1：确认退出')
            if exit_system == '0':
                print('请选择要执行的操作 ')
            elif exit_system == '1':
                break
            else:
                print('请按照提示正确输入')


if __name__ == '__main__':
    start()






