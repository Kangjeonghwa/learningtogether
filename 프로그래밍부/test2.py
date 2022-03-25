x=int(input())
y=int(input())

if x==0 or x<-1000 or x>1000:
    print('-1000 <= x <= 1000이고 x != 0인 x를 입력하세요.')
if y==0 or y<-1000 or y>1000:
    print('-1000 <= y <= 1000이고 y != 0인 y를 입력하세요.')

if x>0:
    if y>0:
        print('1')
    else:
        print('4')
else:
    if y>0:
        print('2')
    else:
        print('3')
