inFp, outFp=None,None
inStr=""
fName1, fName2="",""

fName1=input("소스 파일명을 입력하세요: ")
inFp=open(fName1,"r")

fName2=input("타깃 파일명을 입력하세요: ")
outFp=open(fName2,"w")

inList=inFp.readlines()
for inStr in inList:
    outFp.writelines(inStr)

inFp.close()
outFp.close()
print("%s 파일이 %s 파일로 정상적으로 복사되었음"%(fName1,fName2))