from random import *

aa=[]
N = int(input())
X = int(input())

for i in range(N):
    num=randint(1,10000)
    print(num,end=' ')

    if X > num:
        aa.append(num)

print()

for e in aa:
    print(e, end=' ')
