class human(): #human이라는 클래스 생성
    '''사람'''

person1=human()
person2=human()

person1.language='한국어'
person2.language='english'

print(person1.language)
print(person2.language)

person1.name='한국인'
person2.name='일본인'

def speak(person):
    print('{}이 {}로 말을 합니다'.format(person.name,person.language))

speak(person1)
speak(person2)

human.speak=speak #human클래스에 말하는 능력 추가 -> human class에 speak함수를 넣음 
person1.speak()
person2.speak()