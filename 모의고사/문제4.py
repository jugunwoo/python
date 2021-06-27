def solution(scores):
    grade_counter = [0 for i in range(5)] #grade_counter=[0,0,0,0,0]
    for x in scores: #점수목록에서 하나씩 x에 대입
        if x>=85 and x<=100:  #만약 x가 85점 이상이면
            grade_counter[0] += 1   #학점목록[0]=A학점 한명 추가
        elif x>=70 and x<=84: #만약 x가 70점 이상이면
            grade_counter[1] += 1   #학점목록[1]=A학점 한명 추가
        elif x>=55 and x <=69: #만약 x가 55점 이상이면
            grade_counter[2] += 1   #학점목록[2]=A학점 한명 추가
        elif x>=40 and x<=54: #만약 x가 40점 이상이면
            grade_counter[3] += 1   #학점목록[3]=A학점 한명 추가
        else:                 #아니면
            grade_counter[4] += 1   #학점목록[4]=A학점 한명 추가
    return grade_counter