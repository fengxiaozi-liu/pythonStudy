"""
设计一个名片管理系统
1添加名片
2删除名片
3查询名片
4显示所有名片
5退出程序

"""


class Mingpian:
    def __init__(self):
        self.cache = []
        self.cache1 = {'name': ' ', 'id': 1, 'QQ': 1}

    # 写一个得到名片的格式
    @staticmethod
    def form():
        print('姓名', end='\t')
        print('id', end='\t')
        print('QQ')

    def get_all(self):
        self.form()
        for each_dict in self.cache:
            for each in each_dict.values():
                print(each, end='\t')
            print()

    # 创建一个输入名字的装饰器
    def input_idcard(fn):
        def inner(self,dict1={}):
            count = 0
            count1 = 0
            value = input('请输入你的名字 ')
            dict2 = self.cache1.copy()
            dict2['name'] = value
            print(f'请输入您的id', end=' ')
            value1 = int(input())
            len_cache = len(self.cache)
            if len_cache == 0:
                dict2['id'] = value1
            else:
                for i in range(len_cache):
                    if self.cache[i].get('id') == value1:
                        count += 1
                if count == 0:
                    dict2['id'] = value1
                else:
                    print('您输入的id已经存在，请重新输入')
                    self.exit_mingpian()
            print(f'请输入您的QQ', end=' ')
            value2 = int(input())
            if len_cache == 0:
                dict2['QQ'] = value2
            else:
                for i in range(len_cache):
                    if self.cache[i].get('QQ') == value2:
                        count1 += 1
                if count1 == 0:
                    dict2['QQ'] = value2
                else:
                    print('您输入QQ号码已经存在，请重新输入')
                    self.exit_mingpian()
            return fn(self, dict2)

        return inner

    # 创建添加名片的操作
    @input_idcard
    def tianjia(self, dict1={}):
        self.cache.append(dict1)
        return self

    # 创建一个可以查看名片的操作
    def get_mingpian(self):
        self.form()
        value = int(input('请输入您想要查找id '))
        for each_dict in self.cache:
            if each_dict['id'] == value:
                for each in each_dict.values():
                    print(each, end='\t')

    # 删除名片
    def del_mingpian(self):
        count = 0
        self.form()
        value = int(input('请输入你想要删除的id '))
        for each_dict in self.cache:
            if each_dict['id'] == value:
                count += 1
                print(f'名片{each_dict}已经删除')
                del each_dict
                self.get_all()
        if count == 0:
            print('您输入的id不存在，请仔细核对信息')

    # 退出名片管理系
    def exit_mingpian(self):
        exit('您已将退出了名片管理系统')


m = Mingpian()
m.tianjia().tianjia().get_all()
