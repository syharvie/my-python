import os
print(os.getcwd())
file = None
try:
    file = open('file/致橡树.txt', 'a', encoding='utf-8')
    # print(file.read())
    # for line in file:
    #     print(line, end='')
    # file.close()
    file.write('\n标题<致橡树>')
    file.write('\n作者：舒婷')
    file.write('\n时间：1977年3月')
except FileNotFoundError:    
    print('无法打开指定文件')
except LookupError:
    print('指定了未知的编码')
except UnicodeDecodeError:    
    print('读取文件时解码错误!')
except FileExistsError:
    print('文件不存在')    
finally:    
    if file:
        file.close()

class InputError(ValueError):
    pass


def testInput(a):
    if a > 10:
        raise IndexError('只能输入小于10')
    return a + 10

# try:
#     str = float(input('请输入小于10的数字'))
#     testInput(str)
# except InputError as err:
#     print(err)
# except ValueError:
#     print('输入错误')
try:
    with open('file/avadar.jpg', 'rb') as file1:
        data = file1.read()
    with open('file/avadar2.jpg', 'wb') as file2:
        file2.write(data)
except FileNotFoundError:
    print('指定的文件无法打开')
except IOError:
    print('读写文件错误')
finally:
    print('执行完毕')


import csv
import random
with open('file/scores2.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['姓名', '语文', '数学', '英语'])
    names = ['关羽', '张飞', '赵云', '马超', '黄忠']
    for name in names:
        scores = [random.randrange(50, 101) for _ in range(3)]
        scores.insert(0, name)
        writer.writerow(scores)
