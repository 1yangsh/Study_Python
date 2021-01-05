"""
for문을 이용하여 2~100까지 소수를 출력하는 프로그램
"""
prime_list = []
for i in range(2, 101):
    cnt = 0
    for j in range(i, 0, -1):
        if i % j != 0:
            cnt += 1
    if (i - cnt) == 2:
        prime_list.append(i)

print(f'2~100 사이의 소수 : {prime_list}')
