import random
items = ['小明', '小红', '小青']
items3 = [100, 12.3, 'Python', True]
item4 = items + items3

for i in range(len(items)):
    print(item4[i])

for item in item4:
    print(item)

countsArr = [0] * 6
for _ in range(4000):
    saizi = random.randrange(1,7)
    countsArr[saizi - 1] += 1
for count in range(1, 7):
    print(f'{count}点出现了_{countsArr[count - 1]}次')