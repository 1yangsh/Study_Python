# 클래스 선언
# class MyClass extends Object{}, class MyClass { } -  Java
# class MyClass(object):, class MyClass: - Python

class MyClass(object):
    # constructor 생성자 선언
    def __init__(self):
        # attribute(속성) 초기화
        self.num = 100

    # method(행위) 선언
    def read_number(self):
        return self.num

    # 부모 클래스 (object)가 가진 __str__ 메서드를 재정의
    def __str__(self):
        return f'MyClass의 속성 Num : {str(self.num)}'


# 객체를 생성
my_obj1 = MyClass()
print(my_obj1)
print(my_obj1.read_number())

