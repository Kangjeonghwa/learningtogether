# 교과서 111 페이지 Code03-06.py

def printPoly(t_x,p_x):
    polyStr="P(x) = "

    for i in range(len(p_x)):
        term = t_x[i]
        coef = p_x[i]

        if (coef>=0):
            polyStr+="+"
        polyStr+=str(coef)+"x^"+str(term)+" "
    
    return polyStr

def calcPoly(xVal, t_x,p_x):
    retValue=0

    for i in range(len(px)):
        term = t_x[i]
        coef=p_x[i]
        retValue+=coef*xVal**term
        #term-=1 #이거 필요없는거 아님...?
    
    return retValue


tx=[300,20,0]
px=[7,-4,5]

if __name__=="__main__":

    pStr=printPoly(tx,px)
    print(pStr)

    xValue=int (input("x의 값--> "))

    pxValue=calcPoly(xValue,tx,px)
    print(pxValue)