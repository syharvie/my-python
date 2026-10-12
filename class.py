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

import time

class Clock:
    def __init__ (self, hour=0, minute=0, second=0):
        """
        初始化方法
        Args:
            hour (int, optional): _description_. Defaults to 0.
            minute (int, optional): _description_. Defaults to 0.
            second (int, optional): _description_. Defaults to 0.
        """
        self.hour = hour
        self.min = minute
        self.sec = second
    def run (self):
        self.sec +=1
        if self.sec == 60:
            self.sec = 0
            self.min += 1
            if self.min == 60:
                self.min = 0
                self.hour += 1
                if self.hour == 24:
                    self.hour = 0
    def show (self):
        return f'{self.hour:0>2d}:{self.min:2>2d}:{self.sec:0>2d}'

clock = Clock(4, 12, 32)
while False:
    print(clock.show())
    time.sleep(1)
    clock.run()

class Prop ():
    __slots__ = ('height', '__name')
    def __init__ (self):
        self.__name = '小明'
        self.height = 187

oneperson = Prop()
# oneperson.weight = 100
print(oneperson.height)
print(oneperson._Prop__name)
# print(oneperson.weight)

class Triangel ():
    def __init__ (self,a, b, c):
        self.a = a
        self.b = b
        self.c = c
    @staticmethod
    def is_valid (a, b, c):
        return a + b > c and b + c > a and a + c > b

    @property
    def perimeter (self):
        return self.a + self.b + self.c

    @property
    def area (self):
        p = self.perimeter / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
     
if  Triangel.is_valid(3,4,5):
    t = Triangel(3,4,5)
    print(f'周长{t.perimeter}')
    print(f'面价{t.area}')
else:
    print('无效的边长')

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
    def study(self, course_name):
        print(f'学生：{self.name}正在学习{course_name}')

student1 = Student('小明', 18)
student1.study('数学')


from enum import Enum

class Suite(Enum):
    SPADE, HEART, CLUB, DIAMOND = range(4)
class Card:
    def __init__(self, suite, face):
        self.suite = suite
        self.face = face
    def __repr__(self):
        suites = '♠♥♣♦'
        faces = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        return f'{suites[self.suite.value]}{faces[self.face]}'  # 返回牌的花色和点数
    def __lt__(self, other):
        if self.suite == other.suite:
            return self.face < other.face
        return self.suite.value < other.suite.value
import random
class Poker():
    def __init__(self):
        self.cards = [Card(suite, face)
                      for suite in Suite
                      for face in range(1, 14)]
        self.current = 0
    def shuffle(self):
        self.current = 0
        random.shuffle(self.cards)
    def deal(self):
        card = self.cards[self.current]
        self.current +=1
        return card
    @property
    def has_next(self):
        return self.current < len(self.cards)
    
class Player():
    def __init__(self, name):
        self.name = name
        self.cards = []
    def got_one(self, card):
        self.cards.append(card)
    def arrange(self):
        self.cards.sort()

poker = Poker()
poker.shuffle()
players = [Player('东邪'),Player('西毒'),Player('南帝'),Player('北丐')]

for _ in range(13):
    for player in players:
        player.got_one(poker.deal())
for player in players:
    player.arrange()
    print(f'{player.name}:',  end='')
    print(player.cards)