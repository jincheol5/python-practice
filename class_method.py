#메소드(Method)
#메소드는 함수와 비슷하다.
#클래스에 묶여서 클래스의 인스턴스와 관계되는 일을 하는 함수


#초기화 함수
#__init__ : 인스턴스를 만들 때 실행되는 함수
#문자열화 함수
#__str__ : 인스턴스 자체를 출력 할 때의 형식을 지정해주는 함수
class Human( ):
    '''인간'''

    def __init__( self, name, weight ): #__ = 파이썬에서 특별한 메소드라는 뜻,인스턴스 만들어지는 동시에 같이 돌아감 
        '''초기화 함수'''
        self.name = name
        self.weight = weight
    #번거롭게 creat함수 안만들어도 된다
    def __str__( self ):
        '''문자열화 함수'''
        return "{} ( 몸무게 {}kg )".format( self.name, self.weight )




    """"
    def create( name, weight ): # 다음 강의에서 자세히 설명
        person = Human()
        person.name = name
        person.weight = weight
        return person
    """

    def eat( self ):
        self.weight += 0.1
        print("{}가 먹어서 {}kg이 되었습니다".format(self.name, self.weight))

    def walk( self ):
        self.weight -= 0.1
        print("{}가 걸어서 {}kg이 되었습니다".format(self.name, self.weight))

    def message(self,msg):
        print(msg)

person = Human("철수", 60.5)# 초기화 함수 사용
print( person ) # 문자열화 함수 사용
person.eat()  # 메소드 호출,self로 받기 때문에 매개변수를 따로 넣지 않는다.
person.message('진철이의 코딩공부')