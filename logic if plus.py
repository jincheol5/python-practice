a=10
if a>0 and a%2==0: #두개의 조건 모두 참일 경우에만 실행 
    print('{}는 정답'.format(a))


def return_false():
    print("false 반환")
    return False

def return_true():
    print('true 반환')
    return True

print('test start')
a=return_false()
b=return_true()
if a and b:
    print(True)
else:
    print(False)

print('test2 start')
if return_false() and return_true():  # 첫 번째 조건식이 false여서 뒤의 조건은 확인 X
    print(True)
else:
    print(False)


dic={'key2':3}

if 'key1' in dic and dic['key1']==3: #단락 평가 , and 양 옆의 조건식의 순서를 바꾸면 에러 
    print('key1도 있고 값은 3이네')
else:
    print('아니네')

"""
bool 값과 논리연산
bool() 함수 
true, false
숫자 0을 제외한 모든 수 - true
빈 딕셔너리, 빈 리스트를 제외한 모든 딕셔너리, 리스트 - true
아무 값도 없다는 의미인 None - false
빈문자열을 제외한 모든 문자열 - true
"""
if []:
    print("[]은 True입니다.")

if [1, 2, 3]:
    print("[1,2,3]은/는 True입니다.")

if {}:
    print("{}은 True입니다.")

if {'abc': 1}:
    print("{'abc':1}은 True입니다.")

if 0:
    print("0은/는 True입니다.")

if 1:
    print("1은 True입니다.")

"""
A and B
A 가 false 이면 A 값 따름 
A 가 true 이면 B 값 따름 
A or B 
A가 true 라면 A값 따름 
A 가 false 이면 B 값 따름 
"""

#단락 평가 이해하기 
value = input('압력 해 주세요>') or '아무것도 못 받았어'
print(value)
