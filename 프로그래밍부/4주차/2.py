# 4주차 그리디 알고리즘 Q2

# 빼기 1
def subtract1(N):
    global cnt
    N-=1
    cnt=cnt+1
    return N

# N/k
def NdivK(N,k):
    global cnt
    N=N/k
    cnt=cnt+1
    return N


#메인함수
cnt=0
N,k=input().split()
N=int(N)
k=int(k)

while(N!=1):    # N이 1이 될때까지
    if(N%k==0):
        N=NdivK(N,k)
    else:
        N=subtract1(N)

print(cnt)