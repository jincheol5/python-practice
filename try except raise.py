"""
try:
    # 에러가 발생할 가능성이 있는 코드
except Exception: # 에러 종류
    #에러가 발생 했을 경우 처리할 코드
 """
text='100%'
try:
    number=int(text)
except ValueError:
    print('{}은 숫자가 아닙니다.'.format(text))

def safe_pop_print(list,index):
    try:
        print(list.pop(index))
    except IndexError:
        print('{}의 값을 가져올 수 없습니다.'.format(index))

safe_pop_print([1,2,3],5)

try:
    list=[]
    print(list[0])
except:             #에러의 이름을 모를 때
    print('에러가 발생 했습니다.')


try:
    # 에러가 발생할 가능성이 있는 코드
    list=[]
    print(list[0])
except Exception as ex: # 에러 종류
    print('에러가 발생 했습니다',ex) # ex는 발생한 에러의 이름을 받아오는 변수



#사용자가 직접 에러를 발생시키는 기능
#raise Exception  에러 종류

def rock(mine,yours):
    allowed=['가위','바위','보']
    if mine not in allowed:  #allowed안에 mine이 없으면 
        raise ValueError
    if yours not in allowed:
        raise ValueError
try:
    rock('가위','보자기')
except ValueError:
    print('잘못된 값을 넣은 것 같습니다.')


school={ '1반':[165,166,170,172,180],'2반':[160,170,171,175,183]}

try:
    for class_number,students in school.items():
        for student in students:
            if student>180:
                print('{}에 키가 180이 넘는 학생이 있습니다.'.format(class_number))
                raise StopIteration    #바로 이중 for문 모두 끝내게 하려고 에러 발생시킴
except StopIteration:
    print('정상종료')

#문구점 3곳을 검사하면서 풀이 있으면 문구점의 이름과 가격을 출력합니다.
shops = {
    "송일문방구": {"가위": 500, "크레파스": 3000},
    "알파문구": {"풀": 800, "도화지": 300, "A4용지": 8000},
    "다이소": {"풀": 500, "목공본드": 2000, "화분": 3000}
}
#딕셔너리 활용 

for shop, products in shops.items():
    for product, price in products.items():
        if product =='풀':
            print("{}: {}원".format(shop, price))