# 교과서 433 페이지 Self Study 12-1

from random import *

def bubbleSort(ary):
    global count
    count=0
    n=len(ary)
    for end in range(n-1,0,-1):
        changeYN=False
        #print('#사이클-->',ary)
        for cur in range(0,end):
            if (ary[cur]<ary[cur+1]):
                ary[cur],ary[cur+1]=ary[cur+1],ary[cur]
                changeYN=True
                count+=1
        if not changeYN:
            break
    return ary

dataAry=[randint(0,200) for _ in range(20)]

print('정렬 전 --> ', dataAry)
dataAry=bubbleSort(dataAry)
print('정렬 후 --> ',dataAry)
print('##',count,'회로 정렬 완료')