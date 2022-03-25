#가게 부품 리스트 
N=int(input())
Nlist=list(map(int, input().split()))
Nlist.sort()
#print(Nlist)

if len(Nlist)!=N:
    print("부품 수와 입력 부품 수가 맞지 않습니다.")
    exit()

#요청 부품 리스트
M=int(input())
Mlist=list(map(int, input().split()))

if len(Mlist)!=M:
    print("요청 부품 수와 입력 부품 수가 맞지 않습니다.")
    exit()


#이진 탐색 리스트
def binary_search(array, target, start, end):
    if start>end:
        return False
    mid=(start+end)//2

    if array[mid]==target:
        return True
    elif array[mid]>target:
        return binary_search(array,target,start,mid-1)
    else:
        return binary_search(array,target,mid+1,end)

#메인 함수
for m in Mlist:
    result=binary_search(Nlist,m,0,N-1)
    if result:
        print("Yes",end=' ')
    else:
        print("No",end=' ')
