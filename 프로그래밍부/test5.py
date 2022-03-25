N, K = input().split()
N=int(N);K=int(K)
Klist=[]

if K==1:
    a=input()
    Klist.append(a)
elif K==2:
    a, b = input().split()
    Klist.append(a);Klist.append(b)
elif K==3:
    a, b, c = input().split()
    Klist.append(a);Klist.append(b);Klist.append(c)
else:
    print('1 <= k <= 3인 정수 k 입력')
    quit()

def selectNumber(n):
    if