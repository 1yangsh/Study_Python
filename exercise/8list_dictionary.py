dict1 = {'id': '1',
         'name': 'hong kildong',
         'email': 'hong@mail.com',
         'hp_num': '010-2343-9870'}
dict2 = {'id': '2',
         'name': 'lee soonsin',
         'email': 'lee@mail.com',
         'hp_num': '010-3333-5555'}
dict3 = {'id': '3',
         'name': 'jang yongsil',
         'email': 'jang@mail.com',
         'hp_num': '010-7777-1234'}
dict4 = {'id': '4',
         'name': 'king sejong',
         'email': 'king@mail.com',
         'hp_num': '010-4567-0987'}

list1 = [dict1, dict2, dict3, dict4]

for i in list1:
    for key, val in i.items():
        print(f'key : {key} / value : {val}')
