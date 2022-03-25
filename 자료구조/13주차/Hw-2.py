# 교과서 432 페이지 Code12-02

def bubbleSort(ary):
    n=len(ary)
    for end in range(n-1,0,-1):
        changeYN=False
        print('#사이클-->',ary)
        for cur in range(0,end):
            if (ary[cur]>ary[cur+1]):
                ary[cur],ary[cur+1]=ary[cur+1],ary[cur]
                changeYN=True
        if not changeYN:
            break
    return ary

dataAry=[50,105,120,188,150,162,168,177]

print('정렬 전 --> ', dataAry)
dataAry=bubbleSort(dataAry)
print('정렬 후 --> ',dataAry)