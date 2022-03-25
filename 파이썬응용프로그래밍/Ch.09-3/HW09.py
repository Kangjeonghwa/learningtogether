# HW-9: "두 리스트 의 각 자릿수를 합쳐서 새로운 리스트로 만들기" (강의 비디오 참고)

list1=[1,2,3,4]
list2=[10,20,30,40]
hapList=list(map(lambda n1,n2:n1+n2,list1,list2))
print(hapList)