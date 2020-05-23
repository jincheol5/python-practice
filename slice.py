#slice 리스트나 문자열에서 값을 여러개 가져오는 기능
listt=[1,2,3,4,5]
str='hello world'
print(str[0:5]) #0번째 부터 5번째 전까지 출력 

listt=listt[0:2] #0번째부터 1번째 까지의 리스트를 새로 만듦 
print(listt)

#step slice한 값의 범위에서 step 값을 주어 그 값만큼 건너뛰어 가져오는 기능
#list[ 시작값:끝값:step ]

list1=list(range(20)) #0부터 19까지의 수로 이루어진 리스트를 만들어 주는 함수 
print(list1)
print(list1[::3]) # 3칸씩 건너뛰어서 출력 
list2=list1[5:15:2] # 정해진 범위에서 두칸씩 건너서만 저장 
print(list2)

list3=list1[15:5:-1] #음수로 사용할때는 범위의 위치를 바꿔주어야 한다. -1이여서 역순으로 출력, 
#값도 적당히 바꿔줘야 한다
print(list3)
"""
slice 활용
삭제
del list[ :5 ] : 처음부터 5번째까지 삭제
수정
list[ 1:3 ] = [ 77, 88 ]
list[ 1:3 ] = [ 77, 88 ,99 ] : 더 많은 개수로 변환
list[ 1:4 ] = [ 8 ] : 더 적은 개수로 변환
"""
numbers=list(range(10))
print(numbers)
del numbers[0]
print(numbers)
numbers[0:2]=[11,22] #r값 변경 
print(numbers)
numbers[0:3]=[11,22] # 더 적은 개수로 변환 ,추가도 가능 
del numbers[:5] # 5번째까지 삭제 
print(numbers)
