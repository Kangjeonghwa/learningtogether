# 교과서 110 페이지 Self-study 3-2

def printPoly(p_x):
    term=len(p_x)-1
    polyStr="P(x) = "

    for i in range(len(p_x)):
        coef=p_x[i]

        if (coef>0):
            if(i!=0):
                polyStr+="+"
        if (coef!=0):
            polyStr+=str(coef)+"x^"+str(term)+" "
        term-= 1
    
    return polyStr

px =[7,-4,0,5]

if __name__=="__main__":

    pStr = printPoly(px)
    print(pStr)