# 교과서 230 페이지   응용예제 02

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

SIZE=100
stack=[None for _ in range(SIZE)]
top=-1

if __name__=="__main__":

    with open("fff.txt", "r",encoding="UTF8") as jin:
        lineAry=jin.readlines()
    
    print("--------원본--------")
    for line in lineAry:
        push(line)
        print(line,end=' ')
    print()

    print("--------결과--------")
    for i in lineAry:
        line=pop()
    
        miniStack=[None for _ in range(len(line))]
        miniTop=-1

        for ch in line:
            miniTop+=1
            miniStack[miniTop]=ch
        
        for i in line:
            ch=miniStack[miniTop]
            miniTop-=1
            print(ch,end=' ')
    print()