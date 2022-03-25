n=int(input())
numList=[]
sum, total, cnt=0,0,0

for i in range(n):
    num=int(input())
    numList.append(num)

numList.sort()

for i in numList:
    sum+=i
    if cnt!=0:
        total+=sum
    cnt+=1

print(total)