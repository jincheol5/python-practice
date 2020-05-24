
#오버라이드(Override)
#같은 이름을 가진 메소드를 덮어 쓴다는 의미


class Animal( ): #부모 클래스 
    def walk( self ):
        print( "걷는다" )

    def eat( self ):
        print( "먹는다" )

    def greet( self ):
        print( "인사한다" )

class Human( Animal ):    
    def wave( self ):
        print( "손을 흔든다" )
    def greet( self ): #부모 클래스의 인사한다를 출력 안하고 손을 흔든다로 덮어씀 
        print( "손을 흔든다" )

class Dog( Animal ):    
    def wag( self ):
        print( "꼬리를 흔든다" )
    def greet( self ): #부모 클래스의 인사한다를 출력 안하고 꼬리를 흔든다로 덮어씀
        print( "꼬리를 흔든다" )


person=Human()
dog=Dog()
person.walk()
person.eat()
person.wave()
dog.walk()
dog.eat()
dog.wag()