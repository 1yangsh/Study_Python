"""
list comprehension
"""
books = list() # 책 목록 선언

books.append({'제목': '개발자의 코드', '출판연도': '2013.02.28', '출판사': 'A출판', '쪽수': 200, '추천유무': False})
books.append({'제목': '클린코드', '출판연도': '2013.03.04', '출판사': 'B출판', '쪽수': 584, '추천유무': True})
books.append({'제목': '빅데이터 마케팅', '출판연도': '2014.07.02', '출판사': 'A출판', '쪽수': 296, '추천유무': True})
books.append({'제목': '구글드', '출판연도': '2010.02.10', '출판사': 'B출판', '쪽수': 526, '추천유무': False})
books.append({'제목': '강의력', '출판연도': '2013.12.12', '출판사': 'C출판', '쪽수': 248, '추천유무': True})

page_list = [val['제목'] for val in books if val['쪽수'] > 250]
print(f'250쪽 넘는 책 : {page_list}')

recommend_book = [val['제목'] for val in books if val['추천유무']]
print(f'추천하는 책 : {recommend_book}')

book_publisher = set([val for i in books for key, val in i.items() if key == '출판사'])
print(f'출판사 : {book_publisher}')