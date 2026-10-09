s1 = 'hello, world!'
s2 = "你好，世界！❤️"
s3 = '''hello,
wonderful
world!'''
s4 = '\u9a86\u660a'
print(s1)
print(s2)
print(s3)
print(ord('石'))
print('你' in  s2)
print(s1.capitalize())
print(s1.find('or'))
print(s1.index('or', 1))
print(s1.center(30, '*'))
print(s1.rjust(20))
print(s1.ljust(20, '~'))
print('33'.zfill(20))

a1 = '  你K'
b1 = '他'
print('{0}不是{1}'.format(a1, b1))
print(f'{a1}你不是{b1}，是{a1}')
print(a1.strip('K'))
print(a1.replace('K', 'VV'))
print()
a2 = 'hello word'
wordList = a2.split()
print(wordList)
print('-'.join(wordList))
