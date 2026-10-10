class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def study (self, course_name):
        print(f'{self.name}正在学习{course_name}')
    def play (self):
        print(f'{self.name}正在玩耍')
stu1 = Student('小明', 18)
stu2 = Student('小红', 18)

stu1.study('数学')
stu2.play()