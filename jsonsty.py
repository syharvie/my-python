import json
my_dict = {
    'name': '小石',
    'age': 40,
    'frends': ['xiaoming', 'xiaohong'],
    'cars': [
        {'brand': 'BMW', 'max_speed': 240},
        {'brand': 'Audi', 'max_speed': 280},
        {'brand': 'Benz', 'max_speed': 280}
    ]
}
with open('data.json', 'w') as file:
    json.dump(my_dict, file)
print('------------')    
with open('data.json', 'r') as jsonfile:
    print(json.load(jsonfile))

import requests
apiKey = 'c2f9c82de11606d664a62e8b5727d1db'
resp = requests.get('http://api.tianapi.com/guonei/?key=' + apiKey + '&num=10')
if resp.status_code == 200:
    data_model = resp.json()
    for news in data_model['newslist']:
        print(news['title'])
        print(news['url'])
        print('-' * 60)
