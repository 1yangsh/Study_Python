"""
    섭씨를 입력 받아서 화씨로 변환하는 프로그램
"""


def fah_convert(value) :
    fah = ((9 / 5) * float(value)) + 32
    return fah

print("화씨온도로 변환하고 싶은 섭씨온도를 입력하세요 : ", end="")
deg = input()
fah = fah_convert(deg)

print("섭씨온도 :", deg)
print("화씨온도 : {:.2f}".format(fah))
