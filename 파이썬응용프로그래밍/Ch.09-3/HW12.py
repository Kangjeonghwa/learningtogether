# HW-12: "팩토리얼(Factorial)값을 구하는 함수" (강의 비디오 참고)

def factorial(num):
    if num<=1:
        return num
    else:
        return num*factorial(num-1)

print(factorial(4))
print(factorial(10))