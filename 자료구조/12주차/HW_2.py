# 교과서  페이지  Self Study 11-1

def findMaxIdx(ary):
    maxIdx=0
    for i in range(1,len(ary)):
        if (ary[maxIdx]<ary[i]):
            maxIdx=i
    return maxIdx

testAry=[55,88,33,77]
maxPos=findMaxIdx(testAry)
print('최솟값-->',testAry[maxPos])