# 클래스 선언
# class MyClass extends Object{}, class MyClass { } -  Java
# class MyClass(object):, class MyClass: - Python

class MyClass(object):
    # constructor 생성자 선언
    def __init__(self):
        # attribute(속성) 초기화
        self.num = 100
        self.__name = 'dooly' # private 속성

    # method(행위) 선언
    def read_number(self):
        return self.num

    # 부모 클래스 (object)가 가진 __str__ 메서드를 재정의
    def __str__(self):
        return f'MyClass의 속성 Num : {str(self.num)}'

    # getter method
    @property
    def name(self):
        return self.__name

    # setter method
    @name.setter
    def name(self, new_name):
        if len(new_name) == 3:
            self.__name = new_name
        else:
            print('새로운 이름의 길이는 3 이어야 합니다.')

# 객체를 생성
my_obj1 = MyClass()
print(my_obj1)
print(my_obj1.read_number())

# getter method 호출
print(my_obj1.name)   # property로 생성된 메서드는 () 붙이지 않는다
my_obj1.num = 10
print(my_obj1.num)

# setter method 호출
my_obj1.name = '길동'
print(my_obj1.name)
print(my_obj1.read_number())