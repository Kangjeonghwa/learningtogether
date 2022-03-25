# 교과서 104 페이지 Self-study 3-1

katok =['다현','정연','쯔위','사나','지효']

def delete_data(position):

    if position < 0 or position>len(katok):
        print("데이터를 삭제할 범위를 벗어났습니다!")
        return
    
    kLen=len(katok)
    #katok[position]=None

    for i in range(position,kLen):
        #katok[i-1]=katok[i]
        #katok[i]=None
        katok.pop()
    
    #del(katok[kLen-1])


delete_data(1)
print(katok)