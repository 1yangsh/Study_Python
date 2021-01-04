import random
guess_number = random.randint(1, 100)
cnt = 1
while 1:
    num = int(input("1~100 사이의 숫자를 입력하세요 : "))
    if num == guess_number :
        break
    elif num > guess_number :
        print('숫자가 너무 큽니다.')
    elif num < guess_number :
        print('숫자가 너무 작습니다.')
    cnt += 1

print(f'정답은 {guess_number} 입니다. {cnt}번 만에 맞추셨습니다.')