# 교과서 117 페이지 응용 예제 2

def printPoly(p_x):
    polyStr="P(x) = "

    for i in range(len(p_x[0])):
        coef=p_x[0][i]
        term=p_x[1][i]

        if (coef>=0):
            polyStr+="+"
        polyStr+=str(coef)+"x^"+str(term)+" "

    return polyStr

def calcPoly(xVal,p_x):
    retValue=0

    for i in range(len(p_x[0])):
        coef=p_x[0][i]
        term=p_x[1][i]

        retValue+=coef*xVal**term
    
    return retValue

px=[[7,-4,5],
[300,20,0]]

if __name__=="__main__":

    pStr=printPoly(px)
    print(pStr)

    xValue=int (input("x의 값--> "))

    pxValue=calcPoly(xValue,px)
    print(pxValue)