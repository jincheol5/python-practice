
#유용한 계산식들

areas=[]
for i in range(1,11):  # 1부터 10 까지 
    areas=areas + [i*i]

print(areas)

areas2=[ i*i for i in range(1,11) ]  #계산식 for문 
print('areas2',areas2)


areas3=[]
for i in range(1,11):# 1부터 10 까지 
    if i%2==0:
        areas3=areas3 + [i*i]

print(areas3)

areas4=[ i*i for i in range(1,11) if i%2==0 ]  #계산식 for문 
print('areas4',areas4)

areas5=[ ( x, y ) for x in range(15) for y in range(15) ] # [ 계산식 for문 for문 ]
print(areas5)