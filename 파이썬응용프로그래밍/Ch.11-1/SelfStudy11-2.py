inFp=None
inList,inStr=[],""
cnt=1

inFp=open("C:\\Temp\\data1.txt","r")

inList=inFp.readlines()
for inStr in inList:
    print("%d: %s"%(cnt,inStr),end='')
    cnt+=1

inFp.close()