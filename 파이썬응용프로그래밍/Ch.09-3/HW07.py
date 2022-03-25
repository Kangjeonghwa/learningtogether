# HW-7: "람다 함수와 map() 함수로 간단히" (강의 비디오 참고)

myList=[1,2,3,4,5]
add10=lambda num:num+10
myList=list(map(add10,myList))
print(myList)