# 교과서 473 페이지 Self Study 13-2

from random import randint
from typing import Counter


def binSearch(ary,fData):
    pos=-1
    start=0
    end=len(ary)-1
    count=0

    while(start<=end):
        mid=(start+end)//2
        if fData==ary[mid]:
            count+=1
            return mid, count
        elif fData>ary[mid]:
            start=mid+1
            count+=1
        else:
            end=mid-1
            count+=1
    
    return pos, count

dataAry=[randint(0,100000) for _ in range(100000)]
findData=randint(0,100000)

print('배열 -->',dataAry)
position, countNum = binSearch(dataAry,findData)
if position==-1:
    print(findData,'이 없네요.')
else:
    print(findData,'(은)는 ',position,'위치에 있음')

print('## ',countNum,'회 검색함')
