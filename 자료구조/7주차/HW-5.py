# 교과서 228 페이지  응용예제 01
import random

def isStackFull():
    global SIZE, stack, top
    if (top >=SIZE-1):
        return True
    else:
        return False

def isStackEmpty():
    global SIZE, stack, top 
    if (top==-1):
        return True
    else:
        return False

def push(data):
    global SIZE,stack,top
    if (top >=SIZE-1):
        print("스택이 꽉 찼습니다.")
        return
    top+=1
    stack[top]=data

def pop():
    global SIZE, stack, top
    if (isStackEmpty()):
        #print("스택이 비었습니다.")
        return None
    data=stack[top]
    stack[top]=None
    top-=1
    return data

def peek():
    global SIZE, stack, top 
    if (isStackEmpty()):
        print("스택이 비었습니다.")
        return None
    return stack[top]

SIZE=10
stack=[None for _ in range(SIZE)]
top=-1

if __name__=="__main__":
    
    stoneArray=["빨강","파랑","주황","초록","보라","노랑"]
    random.shuffle(stoneArray)

    print("과자집 가는 길:", end=' ')
    for stone in stoneArray:
        push(stone)
        print(stone,"-->",end=' ')
    print("과자집")

    print("우리집 가는 길:", end=' ')
    for i in stoneArray:
        stone=pop()
        print(stone,"-->",end=' ')
    print("우리집")