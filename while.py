

#조건이 참인 경우 계속 실행하는 반복문
selected=None
while selected not in ['가위', '바위', '보']:
    selected = input('가위, 바위, 보 중에 선택하세요>')
print("선택된 값 {}".format(selected))

patterns=['가위','바위','보']
length=len(patterns)
i=0
while i<length:    # i가 length보다 작을 시 계속 시행 
    print(patterns[i])
    i=i+1




#break
#반복문을 종료시키는 기능
#continue
#반복문의 나머지 부분을 보지 않고, 반복문의 처음으로 돌아가는 기능
list=[1,2,3,4,5]

i=0
for i in range(len(list)):
    if list[i]%3==0:
        print(list[i])
        break
    i=i+1


i=1
for i in range(10):
    if i%2!=0:
        print(i)
    i=i+1

i=1
for i in range(10):
    if i%2==0:
        continue
    else:
        print(i)
    i=i+1
