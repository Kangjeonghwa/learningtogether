# HW-13: "yield 문 : 함수를 종결하지 않으면서 값을 계속 반환" (강의 비디오 참고)

def genFunc():
    yield 1
    yield 2
    yield 3

print(list(genFunc()))