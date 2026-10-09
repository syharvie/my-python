languages = ['Python', 'SQL', 'Java', 'C++', 'Java', 'JavaScript']
languages.append('Go')
languages.insert(3, 'Kotlin')
if 'Java' in languages:
    print(languages.index('Java'))
    print(languages.count('Java'))
    languages.remove('Java')
    print(languages)
    print(languages.pop(-2))
    print(languages)
    print(languages.clear())
    print(languages)
# 列表生成式
items = []
for i in range(1, 100):
    if i % 3 == 0 or i % 5 == 0:
        items.append(i)
print(items)

items2 = [e+1 for e in range(1, 100) if e % 3 == 0 or e % 5 == 0]
print(items2)

# scores = []
# for _ in range(2):
#     temp = []
#     for i in range(3):
#         match i:
#             case 0: col = '语文'
#             case 1: col = '数学'
#             case 2: col = '英文'
#         score = int(input(f'请输入{col}分数：'))
#         temp.append(score)
#     scores.append(temp)
# print(scores)

# scores2 = [[int(input('请输入成绩')) for _ in range(3)] for _ in range(2)]

import random

red_balls = list(range(1, 34))
blue_balls = list(range(1, 17))
selectBalls = []
for _ in range(6):
    index = random.randrange(len(red_balls))
    selectBalls.append(red_balls[index])
    red_balls.pop(index)
selectBalls.sort()
for ball in selectBalls:
    print(print(f'\033[031m{ball:0>2d}\033[0m', end=' '))
blue_balls = random.randrange(1, 17)
print(f'\033[034m{ball:0>2d}\033[0m')


from rich.console import Console
from rich.table import Table

console = Console()
table = Table(show_header=True)
n = int(input('老板你要多少注号码'))
for col_name in ('序号','红球','蓝球'):
    table.add_column(col_name, justify='center')
red_balls2 = [i for i in range(1, 34)]
blue_balls2 = [i for i in range(1, 17)]
for i in range(n):
    selectBalls2 = random.sample(red_balls2, 6)
    selectBalls2.sort()
    blue_ball2 = random.choice(blue_balls2)
    table.add_row(
        str(i + 1),
        f'[red]{" ".join([f"{ball:0>2d}" for ball in selectBalls2])}[/red]',
        f'[blue]{blue_ball2:0>2d}[/blue]'
    )
console.print(table)