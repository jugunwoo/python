def func_a(s): #점수 리스트를 넣어서 최댓값 구하기
    ret = 0 #최댓갑을 0으로 설정
    for i in s: #점수리스트에 하나씩 i에 대입
        if i > ret: #i가 최대값보다 크면
            ret = i #i는 최대값에 저장
    return ret

def func_b(s): #점수리스트를 넣어서 합계구하기 함수
    ret = 0
    for i in s:
        ret += i
    return ret

def func_c(s): #점수리스트를 넣어서 최솟값 구하기
    ret = 101 #최솟값 101으로 설정
    for i in s: #점수리스트에 하나씩 i에 대입
        if i < ret: #i가 최소값보다 작으면
            ret = i #i는 최소값 저장
    return ret


def solution(scores):
    sum = func_b(scores) #1단계
    max_score = func_a(scores) #2단계
    min_score = func_c(scores) #3단계
    return sum - max_score - min_score #4단계