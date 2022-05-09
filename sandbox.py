from fileinput import filename
from genericpath import exists
import os
import sys

sys.stdout = open('#학점이 표기된 데이터를 저장할 위치', 'w', encoding='utf-8')
filename = '#시험점수가 입력된 데이터 위치'


if os.path.exists(filename):
    inFile = open(filename, 'r', encoding='utf-8')

    def print_header():
            print("학생번호 점수 결석일수 학점")


    print_header()
    inList = inFile.readlines()
    for inStr in inList:
        sep = inStr.rstrip('\n').split(' ')
    
        def grade_calculator(lst):
            grade = int(float(lst[1]))
            days = int(lst[2])
        
    
            if grade>=95:
                rank = 'A+'
            elif grade>=90:
                rank = 'A0'
            elif grade>=85:
                rank = 'B+'
            elif grade>=80:
                rank = 'B0'
            elif grade>=75:
                rank = 'C+'
            elif grade>=70:
                rank = 'C0'
            elif grade>=65:
                rank = 'D+'
            elif grade>=60:
                rank = 'D0'
            elif grade<=59:
                rank = 'F'
            
            if days>=5:
                rank = 'F'


            lst.pop()
            
            lst.append(grade)
            lst.append(rank)
        
        
        def print_rank(lst):
            print(lst[0], lst[1], lst[2], lst[4])
        
    
    
        grade_calculator(sep)
        print_rank(sep)

    inFile.close()



else:
    print('파일이 존재하지 않습니다.')