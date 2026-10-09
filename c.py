import random
answer = random.randrange(1, 200)
count = 0
while True:
    count += 1
    guest = int(input('请输入一个整数：'))
    if guest < answer:
        print('数字比你的大')
    elif guest > answer:
        print('数字比你的小')
    else:
        print('对了')
        break
print(f'你一共猜了{count}次')
