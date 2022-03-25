inFp=None
inStr=""

inFp=open("C:\\Temp\\data1.txt","r")

while True:
    inStr=inFp.readline()
    if inStr=="":
        break
    print(inStr,end='')

inFp.close()