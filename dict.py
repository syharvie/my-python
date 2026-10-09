d1 = {
    '名字': '小石',
    '职业': '战士',
    '种族':  '人类',
    'weight': 180,
}
print(d1)

d2 = dict(name='小黄',  职业='牧师')
print(d2)

d3 = dict(zip('姓名职业', '黄战'))
print(d3)

d4 = {x:x+5 for x in range(1,8)}
print(d4)

print('weight' in d1)
print(d1['weight'])
d1x = d1.keys()
print(d1x)
print(d1.values())
d1ex = d1.items()
for a,b in d1ex:
    print(f'{a}: \t{b}')
d5 = {
    '职业': 'KBZ',
    'weight': 180,
    'height': 182
}
d1 |= d5
print(d1)
print(d1.pop('名字'))
d1.popitem()
print(d1)
print(sorted(d1))
# sentence = input('请输入一段话')
# count = {}
# for ch in sentence:
#     if 'A' <= ch <= 'Z' or 'a' <= ch <= 'z':
#         count[ch] = count.get(ch, 0) + 1
# sortedKeys = sorted(count, key=count.get, reverse=True)
# for key in sortedKeys:
#     print(f'{key} 出现了 {count[key]} 次.')

stocks = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}

stock2 = {key: value for key, value in stocks.items() if value > 100 }
print(stock2)
