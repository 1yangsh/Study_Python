"""
    나이 = 현재년도 - 태어난 년도 + 1
    태어난 년도를 입력 받음 import()

    from 모듈명 import
"""
from datetime import datetime as dt
thisYear = dt.today().year
print(dt.today())

birthYear = int(input("태어난 년도를 입력하세요 : "))
age = thisYear - birthYear + 1

if 17 <= age < 20 :
    print('고등학생 입니다.')
elif 20 <= age < 27 :
    print('대학생 입니다.')
else :
    print('학생이 아닙니다.')