# 교과서 249 페이지  Self Study 7-2

def deQueue():
    global SIZE, queue, front, rear
    if (front==rear):
        print("큐가 비었습니다.")
        return None
    front+=1
    data=queue[front]
    queue[front]=None
    return data

SIZE=4
queue=["화사",None,None,None,None]
front=-1
rear=0

print(queue)
retData=deQueue()
print("추출한 데이터 --->",retData)
print(queue)
retData=deQueue()