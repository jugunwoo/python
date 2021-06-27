def func_a(k):
    sum = 0 #누적합계 변수
    for i in range(k+1):
    #for 변수 in range(~전까지): 변수는 1부터 ~전까지 1씩 증가하면서 반복
        #i는 1부터 k 전까지 반복
        #i는 1부터 K+1 전까지 반복
        sum += i #i를 sum 저장

    return sum

def solution(n, m):
    sum_to_m = func_a(m) #1단계
    sum_to_n = func_a(n-1)#2단계
    answer = sum_to_m - sum_to_n #3단계
    return answer