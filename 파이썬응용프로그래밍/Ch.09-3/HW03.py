# HW-3: def outFunc  (강의 비디오 참고)

def outFunc(v1,v2):
    def inFunc(num1,num2):
        return num1+num2
    return inFunc(v1,v2)
print(outFunc(10,20))