Test = int(input())
grade = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']

for T in range(Test):
    student_num,student = map(int,input().split())
    grade_lst = []

    for sn in range(student_num):
        score = list(map(int,input().split()))
        grade_lst.append(score[0]*0.35 + score[1]*0.45 + score[2]*0.2)
    
    count = 0
    for c in range(student_num):
        if grade_lst[student-1] < grade_lst[c]:
            count += 1
    print(f'#{T+1} {grade[count*10//student_num]}')    
