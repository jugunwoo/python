def solution(floors):
    dist=0
    length=len(floors)
    for i in range(1,length):
        if floors[i]>floors[i-1]: #현재층과 앞전층 비교했을때
            dist += floors[i] - floors[i-1]
        else:
            dist += floors[i-1]- floors[i]
    return dist

floors=[1,2,5,4,2]
ret=solution(floors)
print("solution 함수 반환 값은",ret,"입니다.")