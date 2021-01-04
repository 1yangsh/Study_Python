"""
단수를 입력 받아 구구단 계산
"""

while 1:
    dan = int(input("구구단 몇 단을 계산할까요 (1~9)?"))
    if 1 <= dan <= 9:
        print(f'구구단 {dan}단은 계산합니다.')
        for i in range(1,10):
            print("{}X{} = {}".format(dan, i, dan*i))
    else:
        print('구구단 게임을 종료합니다.')
        break
