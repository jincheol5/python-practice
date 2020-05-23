s='hello world'
print(type(s)) #자료형을 알아보는 함수  결과: <class 'int'>

#클래스 : 함수나 변수들을 모아 놓은 집합체 
#인스턴스 : 클래스에 의해 생성된 객체,인스턴스 각자 자신의 값을 가지고 있다.
#ex> int 라는 class의 numbers라는 instance
f=3.14
print(type(f))
print(type(3.15)) #바로 값을 넣어서 확인도 가능 

print(isinstance(42,int)) #자료형 검사 함수, 42가 정수형int 인지 확인 

my_list = [1, 2, 3]
my_dict = {"풀": 800, "색연필": 3000}
my_tuple = (1, 2, 3)
number = 10
real_number = 3.141592

print(type(my_list))
print(type(my_dict))
print(type(my_tuple))
print(type(number))
print(type(real_number))



list1 = [1, 2, 3]
list2 = [1, 2, 3]

if list1 is list1:   #is 연산, 둘이 같은 인스턴스인지 확인 가능함
    print("당연히 list1과 list1은 같은 인스턴스입니다.")

if list1 == list2:   #==연산, 둘이 같은 값ㅇ르 가지는지 확인 가능함 
    print("list1과 list2의 값은 같습니다.")
    if list1 is list2:
        print("그리고 list1과 list2는 같은 인스턴스입니다.")
    else:
        print("하지만 list1과 list2는 다른 인스턴스입니다.")