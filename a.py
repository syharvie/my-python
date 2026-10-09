a = 100
b = '200'
import math
radius = float(input('请输入圆的半径'))
permieter = 2 * math.pi * radius
area = math.pi * radius ** 2
print(f'你给我{a:.2f} 块钱，我还你{b}块钱')
print(f'周长：{permieter:.2f}')
print(f'面积： {area:.2f}')
