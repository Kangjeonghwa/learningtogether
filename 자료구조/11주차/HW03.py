# 교과서 369 페이지 Code10-03

def addNumber(num):
    if num <=1:
        return 1
    return num+addNumber(num-1)

print(addNumber(10)) 