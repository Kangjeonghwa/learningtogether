# HW-10: "자신이 자신을 호출" (강의 비디오 참고)

def selfCall():
    print('하',end='')
    selfCall()
selfCall()