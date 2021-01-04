def add(x, y):
    return x + y

print(add(10, 20))

add2 = lambda x, y: x + y
print(add2(10, 20))

print((lambda x, y: x + y)(10, 20))

print((lambda x: x ** 2)(10))


# map(함수, list) 함수
double_val = lambda x: x ** 2
print(double_val(2))
my_list = [1, 2, 3, 4, 5]
result = map(double_val, my_list)
print(type(result), result)
result = list(map(double_val, my_list))
print(result)

# my_list를 순회(iterate) 하면서 값을 제곱값으로 매핑하는 함수를 호출
result = list(map(lambda x: x ** 2, my_list))
print(result)


# [1,2,3,4,5], [10,20,30,40,50] 두개의 리스트의 값을 더하기
# [11,22,33,44,55]
# lambda 함수와 map 함수 사용
list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]

print(list(map(lambda x, y: x + y, list1, list2)))
print(list(sum(val) for val in zip(list1, list2)))


# 짝수만 제곱하는 함수
print(list(map(lambda x: x ** 2 if x % 2 == 0 else x, my_list)))

map_obj = map(lambda x: x ** 2, list1)
print(next(map_obj), next(map_obj), list(map_obj))


"""
reduce() 함수
"""
from functools import reduce
print(reduce(lambda x, y: x * y, [1, 2, 3, 4, 5]))

result_str = reduce(lambda prev, curr: prev + curr, ['aa', 'bb', 'cc'])  # join 함수와 동일하게 string 연결
print(result_str)

"""
filter() 함수
"""
my_len = lambda my_str: len(my_str)

print(my_len('hello'), my_len('mypython'))

my_list_str = ['hello', 'mypython', 'Machine', 'Deep', 'DataScience']
print(list(result))
result = filter(my_len, my_list_str)
