def calc(v1,v2,op):
    result=0
    if op=='+':
        result=v1+v2
    elif op=='-':
        result=v1-v2
    elif op=='*':
        result=v1*v2
    elif op=='/':
        result=v1/v2
    elif op=='**':
        result=v1**v2
    
    return result

res=0
var1,var2,oper=0,0,''

var1=int(input("첫번째 수를 입력하세요: "))
oper=input("계산을 입력하세요(+,-,*,/,**): ")
var2=int(input("두번째 수를 입력하세요: "))
if oper=='/':
    if var2==0:
        print("0으로 나누면 안됩니다ㅠㅠ")
    else:
        res=calc(var1,var2,oper)
        print('## 계산기 : %d %s %d = %d'%(var1,oper, var2, res))
else:
    res=calc(var1,var2,oper)
    print('## 계산기 : %d %s %d = %d'%(var1,oper, var2, res))
