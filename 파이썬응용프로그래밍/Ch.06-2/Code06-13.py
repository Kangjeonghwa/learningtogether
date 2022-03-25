# HW-9 : Code06-13

hap,i=0,0

for i in range(1,101):
    hap+=i

    if hap>=1000:
        break

print("1~100의 합계에서 최초로 1000이 넘게 하는 숫자: %d"%i)