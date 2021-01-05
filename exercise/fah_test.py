# 2. import 모듈명 as alias명
import exercise.fahrenheit as fah

# 3. from 모듈명 import 함수명
# from exercise.fahrenheit import fah_convert

# 4. from 모듈명 import *

print("화씨온도로 변환하고 싶은 섭씨온도를 입력하세요 : ", end="")
deg = input()
fah = fah.fah_convert(deg)

print("섭씨온도 :", deg)
print("화씨온도 : {:.2f}".format(fah))
