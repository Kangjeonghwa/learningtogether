# HW-14: "yield 문으로 값을 반환한 후 계속 진행" (강의 비디오 참고)

def genFunc(num):
    for i in range(0,num):
        yield i
        print('제너레이터 진행 중')
        
for data in genFunc(5):
    print(data)