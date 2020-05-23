list1=[1,2,3,4,5]
print(list1.index(3)) #값의 인덱스 값을 알려줌 
list1.extend([6,7,8])
print(list1)
list1.insert(0,11) # 0(index위치)번째 자리에 11이라는 값을 넣는다. 뒤로 밀림 
print(list1)

list1.sort( ) # 값을 순서대로 정렬
print(list1)
list1.reverse( ) # 값을 역순으로 정렬
print(list1)

"""
List와 String
리스트와 문자열은 유사하다.
서로 변환이 가능하다.
list = str.split( ) : 문자열에서 리스트로
" ".join( list ) : 리스트에서 문자열으로
"""

str='hello world' #문자열도 리스트와 비슷 
print(str[0])
a='h' in str #문자열 안에 'h'가 있는지 확인 있으면 true 없으면 false
print(a)
b=str.index('h') #리스트 index 함수와 같음 
print(b)

characters = list("abcde")  #list()함수 이용
print(characters)

strr="hello my name is jincheol oh"
strr_list=strr.split() #공백을 짤라서 리스트를 만듦 (기준 없을 때 )
print(strr_list)
strr_list2=' '.join(strr_list) #공백을 기준으로 다시 문자열 리스트로 만들어주는 함수 ' '.join()
print(strr_list2)


time_str="12:44"
time_str_list=time_str.split(':')  # : 기준으로 잡고 짤라서 리스트 만듦 
print(time_str_list)
time_str_list2=':'.join(time_str_list) # :기준으로 다시 합쳐서 문자열 리스트를 만듦 
print(time_str_list2)