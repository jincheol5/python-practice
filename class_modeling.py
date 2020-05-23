#모델링 : 클래스로 현실의 개념을 표현하는 것
#:을 찍은 뒤에는 무조건 지금보다 1 level 들여쓰기된 코드가 나타나야 합니다.
class human():
    """
    : 뒤에는 무조건 아무 코드나 하나 나와야 함
    안쓰면 들여쓰기 오류 
    """
    



def create_human(name,weight):
    person=human()
    person.name=name
    person.weight=weight
    return person

human.create=create_human


def eat(person):  #먹는 함수 생성, 먹을떄마다 +1kg
    person.weight+=0.1
    print("{}가 음식을 먹어서 {}kg이 되었습니다.".format(person.name,person.weight))



def walk(person): #걷는 함수 생성, 걸을때마다 -1kg
    person.weight-=0.1
    print("{}가 걸어서 {}kg이 되었습니다.".format(person.name,person.weight))

person=human.create('진철',60.5) #person에게 휴먼 클래스 와 create 함수 부여 

human.eat=eat #휴먼 클래스에 먹는 함수 추가
human.walk=walk #휴먼 클래스에 걷는 함수 추가 




person.eat() #person 에게 걷는것을 시키는 것이니깐 따로 매개변수는 안넣어도 된다  ???왜?
person.eat()
person.walk()


#Human 클래스를 선언 후, person = Human.create(~)를 해서 person이 Human클래스의 인스턴스가 된 것
#eat, walk 함수가 정의되고 이게 Human클래스 아래에 Human.eat, Human.walk로 선언되었기에,
#Human.walk() 은 walk(Human)과 같은 실행 결과를 갖게 됨
#person은 Human 클래스의 인스턴스이므로, person.walk()는 walk(person)과 같은 의미를 갖게 되어, 
#결국 person.name과 person.weight를 가지고 walk 함수를 실행시킨 결과가 출력됨.