def square(n,x):
    result=n**x

    return result

def mod(n,m):
    result=n%m
    return result

a=int(input("x 입력: "))
b=int(input("거듭제곱할 수 입력: "))
c=int(input("mod할 수 입력: "))

xy=square(a,b)
print(xy)
result=mod(xy,c)
print(result)
