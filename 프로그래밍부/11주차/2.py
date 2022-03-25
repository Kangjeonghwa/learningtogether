N, M=map(int,input().split())
nlist=[]
cnt=0

for i in range(N):
    num=int(input())
    nlist.append(num)

nlist.sort(reverse=True)

for n in nlist:
    if M>n:
        cnt+=M//n
        M=M%n

if M!=0:
    print("-1")
else:
    print(cnt)