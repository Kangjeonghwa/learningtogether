# 교과서 370 페이지 Self Study 10-1

def addNumber(a,b):
    if(a<=b):
        if (b <=a):
            return 1
        return b+addNumber(a,b-1)
    else:
        if (a <=b):
            return 1
        return a+addNumber(a-1,b)


a=int(input("숫자1-->"))
b=int(input("숫자2-->"))
print(addNumber(a,b)) 