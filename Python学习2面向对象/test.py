class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_person(self):
        temp = []
        temp.extend([self.name, self.age])
        return temp


class Person1(Person):
    def __init__(self, name, age, hobby):
        super().__init__(name, age)
        self.hobby = hobby

    def show_person(self):
        return super().show_person()


p = Person1('zhangsan', 18, '吃饭')
print(p.show_person())
