# 1주차 공통과제 1번

# 숫자 입력
def inputNum():  
    for i in range(10):
        num=int(input())
        numList.append(num)

# 나머지 구하기
def divNum():
    for i in numList:
        d = i%42
        divList.append(d)

# 서로다른 나머지 수 구하기
def sortNum():
    divList.sort()
    removeDuplicate=set(divList)
    resultList=list(removeDuplicate)
    return resultList

numList = []
divList = []

# 메인 함수
if __name__ == "__main__":
    inputNum()
    divNum()
    resultList=sortNum()
    result=len(resultList)

    print(result)
