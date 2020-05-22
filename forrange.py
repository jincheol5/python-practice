#for in list : 순회할 리스트가 정해져 있을 때
#for in range() : 순회할 숫자가 정해져 있을 때 '

for i in range(5):
    print(i)   # 0부터 4까지 

list=['나','너','우리']
for i in range(len(list)):
    print(list[i])

names = ['철수', '영희', '영수']
for i, name in enumerate(names):
    print('{}번: {}'.format(i + 1, name))

#enumerate는 리스트가 있는 경우 순서와 리스트의 값을 전달하는 기능을 합니다. 