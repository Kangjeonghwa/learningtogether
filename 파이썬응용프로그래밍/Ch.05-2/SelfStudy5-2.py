# H/W-5 : Self Study 5-2.py

answer, num1, num2, addNum=0,0,0,0

num1=int(input("***첫 번째 숫자를 입력하세요 : "))
num2=int(input("***두 번째 숫자를 입력하세요 : "))
addNum=int(input("***더할 숫자를 입력하세요 : "))

for i in range(num1,num2+1, addNum):
    answer=answer+i

print("%d+...+%d는 %d입니다."%(num1,num2,answer))