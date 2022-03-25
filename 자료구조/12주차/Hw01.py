# 교과서 374 페이지  Code10-05

def countDown(n):
    if n==0:
        print("발사")
    else:
        print(n)
        countDown(n-1)

countDown(5)