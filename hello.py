



"""
정수와 실수
정수
영어로 integer, 줄여서 파이썬에서는 int라고 표현
정수끼리 더하거나 곱하거나 빼면 정수
정수끼리 나누면 실수가 나올 수 있으나, 나눗샘의 몫만을 구하려면 //연산자를 이용

a = 5//3 #계산결과 a=1
실수를 정수로 바꾸려면 int를 이용

a=int(5.4)라고 하면 a는 5를 값으로 가지게 된다.
실수
부동소수점이라는 표현법을 이용해 소숫점을 표시할 수 있는 숫자
어느정도의 계산 정확도는 가지지만, 계산에 있어서 완벽한 정확성은 가지지 않는다.

0.1+0.1+0.1 == 0.3 #FALSE
정수를 실수로 바꾸려면 float를 사용

a=float(5)라고 하면 a는 5.0을 값으로 가지게 된다.



사용자 입력 받기
프로그래밍의 3단계
사용자 입력
자료 처리
결과 출력
input()
사용자의 키보드 입력을 return


print('가위 바위 보 중 하나를 내주세요> ', end = ' ')
mine = input()
print('mine:', mine)
간단한 print기능을 내장

mine = input('가위 바위 보 중 하나를 내주세요> ')
print('mine:', mine)
Ctrl + c
프로그램 즉시 종료
"""

list1 = ['가위','바위','보']
list2 = [37,23,10,33,29,40]

print(list1)
print(list2)

print(list1[0]) # 0 부터 시작 c 와 동일 프로그래밍 세계에선느 다 0 부터 시작한다
print(list1[-1]) # -1 은 뒤에서 첫번째, -2는 두번째  


list2.append(16)
print(list2)
list3=list2+[16]
print(list3)
list4=list2+list3
print(list4)


#in 연산 
#12라는 값이 리스트에 들어있는지 확인하는 코드
n=12
ownership = n in list3
print(ownership)

a=10
if a in list3:
    print('{}은 있어'.format(a))

del list4[12] #13번째(12번 자리) 값을 지움 
print(list4)
list4.remove(40) #40 이라는 값을 지움 
print(list4)
# 같은 값이 여러게 나와있어도 먼저 나오는 값 하나만 삭제 