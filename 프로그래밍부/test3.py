from random import *

k=int(input())
numlist=[]
sum=0

for i in range(k):
    num = int(input())
    if num != 0:
        numlist.append(num)
    else:
        numlist.pop()

for a in numlist:
    sum+=a

print(sum)