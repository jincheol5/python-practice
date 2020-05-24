#super()
#자식클래스에서 부모클래스의 내용을 사용하고 싶은 경우
#super().부모클래스내용

class Animal( ):
    def __init__( self, name ):
        self.name = name
    def greet(self):
        print('손을 흔든다.')

class Human( Animal ):
    def __init__( self, name, hand ):
        super().__init__( name ) # 부모클래스의 __init__ 메소드 호출
        self.hand = hand
    def greet(self):
        print("{}으로 손을 흔든다.".format(self.hand))

person = Human( "사람", "오른손" )
person.greet()




