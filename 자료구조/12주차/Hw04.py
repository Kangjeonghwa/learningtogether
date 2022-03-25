# 교과서 376 페이지  Self Study 10-2

def gugu(dan,num):
    print("%2d X%2d=%2d" %(dan, num, dan*num), end='  ')
    if dan<10:
        gugu(dan+1,num)
    

for num in range(1,10):
    gugu(2,num)
    print()