import random

list = 1,2,3
num = int(input('digi: '))

for num in range(1,num):
    lis = []
    li = random.choice(list)
    print(li)
    lis.append(li)

print(f'aqui esta: {lis}')
