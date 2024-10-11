class Person:
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex
    def action1(self):
        print(self.name + "在喝水")
    def action2(self):
        print(self.name + '是个' + self.sex)

if __name__ == '__main__':
        p = Person("张三","男")