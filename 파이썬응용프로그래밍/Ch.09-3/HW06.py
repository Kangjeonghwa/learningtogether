# HW-6:"리스트에 모두 10을 더하는 코드" (강의 비디오 참고)

myList=[1,2,3,4,5]
def add10(num):
    return num+10

for i in range(len(myList)):
    myList[i]=add10(myList[i])
print(myList)