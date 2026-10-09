# height  = float(input('请输入身高'))
# weight = float(input('请输入体重'))
# bmi = weight / (height / 100) ** 2
# print(f'你的BMI是：{bmi:.1f}')
# if 18.5 <= bmi < 24:
#     print('你的身材很棒')
# elif bmi < 18.5:
#     print('你太瘦了')
# elif bmi > 24:
#     print('你太胖了')

statusCode = int(input('请输入网络状态码'))
match statusCode:
    case 200: 
        description = '网络正常'
    case 400: 
            description = 'Bad Request'
print(description) 
           