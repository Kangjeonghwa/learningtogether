# 교과서 375 페이지  Code10-06

def printStar(n):
    if n>0:
        printStar(n-1)
        print('★ '*n)

printStar(5)