def func_a(arr, n):
                    #arr:visitor
                    #n:max_first
    ret = [] #새로운 리스트
    for x in arr: #방문객리스트에 하나씩 x에 대입
        if x != n: #x가 최대방문객수와 다르면
            ret.append(x) #새로운 리스트에 저장
    return ret

def func_b(a, b): #첫번째 최대방문객수와 두번째 방문객수
        #a:max_first
        #b:max_second
    if a >= b:
        return a - b    #빼기=차이
    else:
        return b - a    #빼기=차이

def func_c(arr): #방문객 리스트에서 가장 많은 방문객 수를 구하는 함수
    ret = -1 #최대값을 -1으로 저장
    for x in arr: #방문객리스트에서 하니씩 x에 대입
        if ret < x: #x가 최대값보다 크면
            ret = x #x는 최대값에 저장
    return ret

def solution(visitor):
    max_first = func_c(visitor) #1단계
    visitor_removed = func_a(visitor,max_first) #2단계
    max_second = func_c(visitor_removed) #3단계
    answer = func_b(max_first,max_second)
    return answer