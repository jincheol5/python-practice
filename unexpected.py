#unexpectedvalue 파일과 연동 
from unexpectedvalue import unexpectedvalue

value='가'
try:
    if value not in ['가위','바위','보']:
        raise unexpectedvalue

except unexpectedvalue:
    print('에러가 발생했습니다.')




# 이 아래에 Exception을 상속 받는 MyException클래스를 정의하세요.
class MyException(Exception):
    '''예외처리'''
    
shops = {
    "송일문방구": {"가위": 500, "크레파스": 3000},
    "알파문구": {"풀": 800, "도화지": 300, "A4용지": 8000},
    "다이소": {"풀": 500, "목공본드": 2000, "화분": 3000}
}

try:
    for shop, products in shops.items():
        for product, price in products.items():
            if product == '풀':
                print("{}: {}원".format(shop, price))
                raise MyException
except MyException:
    print("풀을 찾았습니다.")