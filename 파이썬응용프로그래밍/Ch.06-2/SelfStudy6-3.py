# HW-2 : Self Study 6-3

i, k, guguLine = 0, 0, ""

for i in range(9,1,-1):
    guguLine+=("#   %i단   #"%i)

print(guguLine)

for i in range(9,1,-1):
    guguLine=""
    for k in range(9,1,-1):
        guguLine+=str("%2d X %2d=%2d "%(k,i,k*i))
    print(guguLine)