inFp=None
inStr=""
cnt=1

inFp=open("C:\\Temp\\data1.txt","r")

while True:
    inStr=inFp.readline()
    if inStr=="":
        break
    print("%d: %s"%(cnt,inStr),end='')
    cnt+=1

inFp.close()