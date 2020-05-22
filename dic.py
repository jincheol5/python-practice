#dictionary
#여러 값을 저장해두고 필요한 값을 꺼내 쓰는 기능
#이름표를 이용하여 값을 꺼내 사용
# 딕셔너리명={
# '이름표1':'값1'
# '이름표2':'값2'
# }

wintable = {
    '가위' : '보',
    '바위' : '가위',
    '보' : '바위',
}

print(wintable['가위'])

days_in_month = {
    #여기에 코드를 완성해 보세요.
    '1월' : 31,
    '2월' : 28,
    '3월' : 31,
    
    
 }

print(days_in_month)


#↓ 이름표는 문자열 또는 숫자를 주로 사용하지만
dict = {     "이름표"    :    [1,2,3] }
#↑ 값은 리스트를 포함해서 무엇이든 올 수 있습니다.

print( dict["이름표"] )


list=[1,2,3,4]
list.append(4) #리스트 추가 
print(list)
list[4]=6 #리스트 수정
print(list)
del(list[4]) #리스트 삭제
print(list)
print(list.pop(3))# 리스트 값 삭제하면서 삭제한 값 리턴 후 출력 pop함수 이용
dec={
'a':1,
'b':2,
'c':3,

}
dec['d']=4   #딕셔너리 추가 
print(dec)
dec['d']=5   #딕셔너리 수정
print(dec)
del(dec['d']) #딕셔너리 삭제
print(dec)
print(dec.pop('c')) # 딕셔너리  삭제하면서 삭제한 값 리턴 후 출력 pop함수 이용

#이름표=key , 값=value

ages={
    'a':12,
    'b':13,
    'c':14,
}

for key in ages.keys():  # keys()=이름표 출력, keys()함수 생략할 경우 이름표 출력으로 나옴 
    print(key)
for value in ages.values(): # values()=값 출력
    print(value)

    #딕셔너리 반복문은 순서에 맞게 출력하지 않는다

for key,value in ages.items():  #items()=딕셔너리에서 두개의 값(이름표,값)을 넘겨줌 
    print("{}의 나이는 {}살".format(key,value))

ages2={

    'f':4,
}

ages.update( ages2 ) #딕셔너리 결합 ages2를 ages에 결합

print(ages)

ages2.clear()  #딕셔너리의 내용 모두  삭제

#튜플 
#한번 정해진 순서를 바꿀 수 없다
#값 변경도 불가능하다
tuple1 = (1, 2, 3, 4)

tuple2 = 1, 2, 3, 4  #() 안써도 똑같이 적용 
 
mylist = [1,2,3,4]
tuple3 = tuple(mylist) #튜플안에 리스트의 값들을 넣는다.

#packing 하나의 변수에 튜플을 이용하여 여러개의 값을 넣는 것
#unpacking 패킹된 변수에서 여러개의 값을 꺼내오는 것

c = (3, 4)
d, e = c    # c의 값을 언패킹하여 d, e에 값을 넣었다
f = d, e    # 변수 d와 e를 f에 패킹

#튜플의 활용
#두 변수의 값을 바꿀 때 임시변수가 필요 없다.
#함수의 리턴 값으로 여러 값을 전달할 수 있다
# ex)  x,y=y,x

list3=[1,2,3,4,5]
for i,v in enumerate(list3):  # 인덱스(0번째....)와 값을 리턴 
    print('{}번째 수 {}'.format(i,v))

for a in enumerate(list3):  # 인덱스(0번째....)와 값을 리턴 
    print('{}번째 수 {}'.format(a[0],a[1]))
#for문을 거칠때마다 a는 (0,1) -> (1,2) -> (2,3) -> (3,4) -> (4,5)로 바뀝니다.
#따라서 a[0]은 0->1->2->3->4가 될거고, a[1]은 1->2->3->4->5가 되겠지요.



for a in enumerate(list3):  # 인덱스(0번째....)와 값을 리턴 
    print('{}번째 수 {}'.format(*a) ) #튜플을 쪼갬 

dic2={
    'a':10,
    'b':11,
    'c':12
}
for key,value in dic2.items():
    print('{}의 나이는 {}살'.format(key,value))
for a in dic2.items():
    print('{}의 나이는 {}살'.format(a[0],a[1]))
