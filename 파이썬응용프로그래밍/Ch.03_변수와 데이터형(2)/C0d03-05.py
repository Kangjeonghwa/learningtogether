# HW-3 교과서 84 페이지 Code03-05.py

from typing import DefaultDict


def myFunc():
    print('함수를 호출함.')

# 전역 변수
gVar = 100

if __name__=='__main__':
    print('메인함수 부분이 실행됩니다.')
    myFunc()
    print('전역 변수 값 :',gVar)

def main():
    print('메인 함수 부분이 실행됩니다.')
    myFunc()
    print('전역 변수 값 :',gVar)

if __name__=='__main__':
    main()