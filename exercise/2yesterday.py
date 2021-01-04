"""
yesterday.txt 파일을 읽어서
YESTERDAY 라는 단어가 몇번 나왔는지
Yesterday 라는 단어가 몇번 나왔는지
yesterday 라는 단어가 몇번 나왔는지
"""

# yesterday.txt 파일 읽기
f = open('yesterday.txt', 'r')
yesterday_lyric = f.read()
f.close()


# file read 를 함수로 선언
def file_read(file_name) :
    with open(file_name, 'r') as f:
        lyric = f.read()
        print(lyric)
    return lyric

# 함수 호출
yesterday_lyric = file_read('yesterday.txt')


# YESTERDAY 라는 단어의 횟수
print('YESTERDAY 라는 단어의 횟수 : {}'.format(yesterday_lyric.upper().count('YESTERDAY')))

# Yesterday 라는 단어의 횟수
print('Yesterday 라는 단어의 횟수 : {}'.format(yesterday_lyric.count('Yesterday')))

# yesterday 라는 단어의 횟수
print('yesterday 라는 단어의 횟수 : {}'.format(yesterday_lyric.count('yesterday')))