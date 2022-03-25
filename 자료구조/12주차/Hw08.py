# 교과서 380 페이지  Code10-11

def palindrome(pStr):
    if len(pStr)<=1:
        return True
    
    if pStr[0]!=pStr[-1]:
        return False
    
    return palindrome(pStr[1:len(pStr)-1])

strAry=["reaver","kayak","borrow or rob","주유소의 소유주","야 너 이번 주 주번이 너야","살금 살금"]

for testStr in strAry:
    print(testStr,end='-->')
    testStr=testStr.lower().replace(' ','')
    if palindrome(testStr):
        print("O")
    else:
        print("X")