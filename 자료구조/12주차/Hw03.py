# 교과서 375 페이지  Code10-07

def gugu(dan,num):
    print("%d X %d = %d" %(dan, num, dan*num))
    if num<9:
        gugu(dan,num+1)
    

for dan in range(2,10):
    print("## %d 단 ##" %dan)
    gugu(dan,1)