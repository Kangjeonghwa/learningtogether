# 교과서 115 페이지 응용 예제 1

def add_friend(name, tokNum):
    pos=len(katok)

    for i in range(len(katok)):
        tokList=katok[i]    #tokList는 원래 카톡 튜플
        
        if tokNum>= tokList[1]: #카톡 횟수 비교
            pos=i
            break
    
    katok.insert(pos, (name,tokNum))    #리스트에 삽입

katok=[('다현',200),('정연',150),('쯔위',90),('사나',30),('지효',15)]

if __name__=="__main__":

    while True:
        name=input("추가할 친구-->")
        tokNum=int(input("카톡횟수--> "))
        add_friend(name,tokNum)

        print(katok)