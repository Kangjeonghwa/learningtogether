# 교과서 437 페이지 Self Study 12-2
from random import *

def quickSort(ary):
    global count
    

    n=len(ary)
    if n<=1:
        return ary
    
    pivot=ary[n//2]
    leftAry,rightAry=[],[]

    for num in ary:
        if num>pivot:
            leftAry.append(num)
            count+=1
        elif num<pivot:
            rightAry.append(num)
            count+=1

    return quickSort(leftAry)+[pivot]+quickSort(rightAry)

dataAry=[randint(0,200) for _ in range(20)]
count=0

print('정렬 전 --> ', dataAry)
dataAry=quickSort(dataAry)
print('정렬 후 --> ',dataAry)

print('##',count,'회로 정렬 완료')