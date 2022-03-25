# 1번 문제
import collections

n = int(input())    #학생 수 n 입력

student={}          #학생 딕셔너리 생성
studentList=[]      #학생 리스트 생성


for i in range(n):                  #학생 수 n만큼 입력받아 공백으로 분리하여 변수에 저장
    name,score=input().split()
    student[name]=int(score)        #각각 딕셔너리에 key와 value로 저장

studentList=sorted(student.items(), key=lambda x:x[1])      #딕셔너리의 결과를 점수인 value로 오름차순 정렬하여 학생 리스트에 저장

for i in studentList:
    print(i[0],end=' ')