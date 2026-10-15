import xlrd
wb = xlrd.open_workbook('file/阿里巴巴2020年股票数据.xls')
sheetsnames = wb.sheet_names()
print(sheetsnames)
sheet = wb.sheet_by_name(sheetsnames[0])
print(sheet.ncols, sheet.nrows)
for row in range(sheet.nrows):
    for col in range(sheet.ncols):
        value = sheet.cell(row, col).value
        if row > 0:
            if col == 0:
                value = xlrd.xldate_as_tuple(value, 0)
                value = f'{value[0]}年{value[1]:>02d}月{value[2]:>02d}日'
            else:
                value = f'{value:.2f}'
        # print(value, end='\t')
# 0 - 空值，1 - 字符串，2 - 数字，3 - 日期，4 - 布尔，5 - 错误    
last_cell_type = sheet.cell_type(sheet.nrows - 1,  sheet.ncols - 1)
print(last_cell_type)
print(sheet.row_values(1))
print(sheet.row_slice(1, 0, 4))


import random
import xlwt
student_names = ['关羽', '张飞', '赵云', '马超', '黄忠']
scores = [[random.randrange(0, 100) for _ in range(3)] for _ in range(5)]
print(scores)
wb = xlwt.Workbook()
head_style = xlwt.XFStyle()
pattern = xlwt.Pattern()
pattern.pattern = xlwt.Pattern.SOLID_PATTERN
# 0 - 黑色、1 - 白色、2 - 红色、3 - 绿色、4 - 蓝色、5 - 黄色、6 - 粉色、7 - 青色
pattern.pattern_fore_colour = 3
head_style.pattern = pattern
font = xlwt.Font()
font.name = '华文楷体'
font.height = 20 * 18
font.bold = True
font.italic = False
font.colour_index = 1
head_style.font = font
sheet = wb.add_sheet('终极三国班')
titles = ('姓名', '语文', '数学', '英语')
for index,title in enumerate(titles):
    sheet.write(0, index, title, head_style)
for row in range(len(scores)):
    sheet.write(row + 1, 0, student_names[row])
    for col in range(3):
        sheet.write(row + 1, col + 1, scores[row][col])
wb.save('file/终极三国班.xls')
