"""
    문자열 관련 내용
"""

# escape 문자
greet = "Hello" * 4 + '\n'
end = '\tGood \'Bye\' !!'
end2 = "\t Good 'Morning' ??"
print(greet + end + end2)

# boolean 타입과 str 타입
is_flag = False
my_str = "False"
print(type(is_flag), type(my_str))
if not is_flag :
    print(my_str)

# 문자열 인덱스(오프셋)
#           01234567891011
greeting = 'HELLO WORLD!'
# C언어 스타일
print("문자열 길이 %i" % len(greeting))   # 변수 타입을 알아야 하기 때문에 비효율적
print("문자열 길이", len(greeting))       # 비효율적인 방법

print("문자열 길이 {}, 0번째 인덱스 값은 {}".format(len(greeting), greeting[0]))
print('0번째 인덱스 값은 {1} , 문자열의 길이 {0}'.format(len(greeting), greeting[0]))
# 파이썬 3.6 버전 이후
print(f"문자열 길이 {len(greeting)}, 1번째 인덱스 값은 {greeting[1]}")

# IndexError: string index out of range
# print(greeting[12])

# 문자열 인덱스 슬라이싱 [start:end:step] step은 default 로 1 이다. (end값은 exclusive)
print(f"greeting[0:5] = {greeting[0:5]}") # 01234
print(f"greeting[6:12] = {greeting[6:12]}") # 67891011
print(f"greeting[6:] = {greeting[6:]}")  # 6이후 부터
print(f"greeting[:5] = {greeting[:5]}")  # 5이전
print(greeting, greeting[:])
print(greeting[::2])  # HLOWRD (몇칸씩 걸처 출력할지)
# 음수값의 인덱스
print(f'greeting[-1:] = {greeting[-1:]}')
print(f'greeting[-2:] = {greeting[-2:]}')
# 문자열이 역순으로 바뀐다
print(f'greeting[::-1] = {greeting[::-1]}')

# 문자열 여러가지 함수들
word = 'Good manufacturing Practice Good'
print(f'대문자로 변환 = {word.upper()}')
result = word.upper()
print(word, '\t', result)
print(f'소문자로 변환 = {word.lower()}')
print(word.title())
print(word.find('m'), word.rfind('m'))
print(word.find('G'), word.rfind('G'))
print(word.count('G'))
word_list = word.split()
print(word_list, type(word_list))
word2 = 'Good/manufacturing/Practice/Good'
print(word2.split('/'))

word3 = ' hello python '
print(len(word3), len(word3.strip()), word3.strip())
print(len(word3.rstrip()), word3.rstrip())

print(word.startswith('G'))
print(word.endswith('G'))

for val in word :
    print(val, word.count(val))

print(word_list)
for w in word_list :
    print(w)




