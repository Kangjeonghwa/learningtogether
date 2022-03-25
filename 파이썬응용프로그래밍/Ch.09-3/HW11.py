# HW-11: "입력한 숫자를 1까지 세는 함수를 재귀 함수" (강의 비디오 참고)

def count(num):
    if num>=1:
        print(num,end=' ')
        count(num-1)
    else:
        return print()
count(10)
count(20)