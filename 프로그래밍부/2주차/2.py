# 2주차 공통과제 2번

# 재귀함수
def printStar(n):
    global star

    if n==3:
        star[0][:3]=star[2][:3]=['*']*3
        star[1][:3]=['*', ' ', '*']
        return
    
    a=n//3
    printStar(a)

    for i in range(3):
        for j in range(3):
            if i ==1 and j==1:
                continue
            for k in range(a):
                star[a*i+k][a*j:a*(j+1)]=star[k][:a]

# 메인 함수
N = int(input())
star=[[' ' for i in range(N)] for i in range(N)]

printStar(N)

for i in range(N):
    for j in range(N):
        print(star[i][j],end=' ')
    print()