# 2.
# 회문(palindrome)? 순서를 거꾸로 해서 읽어도 제대로 읽을때와 같은 단어 or 문장
# rotator, sos, abba (nurses run)
# 문제: 임의의 단어(문장)을 입력받아 회문 여부를 출력 => True or False 출력


pal = input("단어 혹은 문장을 입력하세요 : ")
pal2 = ""

for i in pal:  # pal = nurses run
    if i != " ":
        pal2 += i  # pal2 = nursesrun

if pal2 == pal2[::-1]:
    print("True")
else:
    print("False")


