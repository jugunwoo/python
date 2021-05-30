import math

def solution(N,M):
    total=0
    for x in range(N,M-1):
        if x %2==0:
            #==0 짝수   ==1 홀수
            total+=x*x
            #수*수=제곱

    return total

N=4
M=7

ret=solution(N,M)
print("solution 함수와 결과",ret,"입니다.")