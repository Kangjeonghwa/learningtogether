aa=[]
bb=[]
value=1
for i in range(0,3):
    for k in range(0,4):
        aa.append(value)
        value+=1
    bb.append(aa)
    aa=[]

for i in range(0,3):
    for k in range(0,4):
        print("%3d"%bb[i][k],end=' ')
    print(" ")