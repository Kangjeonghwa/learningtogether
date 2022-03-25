# 교과서 476 페이지 Code13-04
from operator import itemgetter

def makeIndex(ary,pos):
    beforeAry=[]
    index=0
    for data in ary:
        beforeAry.append((data[pos],index))
        index+=1
    
    sortedAry=sorted(beforeAry,key=itemgetter(0))
    return sortedAry

def bookSearch(ary,fData):
    pos=-1
    start=0
    end=len(ary)-1

    while(start<=end):
        mid=(start+end)//2
        if fData==ary[mid][0]:
            return ary[mid][1]
        elif fData>ary[mid][0]:
            start=mid+1
        else:
            end=mid-1
    
    return pos

bookAry=[['어린왕자','생택쥐페리'],['이방인','까뮈'],['부활','톨스토이'],['신곡','단테'],['돈키호테','세르반테스'],['동물농장','조지오웰'],['데미안','헤르만헤세'],['파우스트','괴테'],['대지','펄벅']]
nameIndex=[]
authIndex=[]

print('# 책장의 도서 ==>', bookAry)
print()
nameIndex=makeIndex(bookAry,0)
print('# 도서명 색인표 ==>',nameIndex)
print()
authIndex=makeIndex(bookAry,1)
print('# 작가면 색인표 ==>',authIndex)
print()

findName='신곡'
findPos=bookSearch(nameIndex,findName)
if findPos!=-1:
    print(findName,'의 작가는',bookAry[findPos][1],'입니다.')
else:
    print(findName,' 책은 없습니다.')

findName='괴테'
findPos=bookSearch(authIndex,findName)
if findPos!=-1:
    print(findName,'의 작가는',bookAry[findPos][0],'입니다.')
else:
    print(findName,' 작가는 없습니다.')
