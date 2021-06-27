#리스트=[ ]
#2차원리스트=[ [ ] , [ ] , [ ] ]




def solution(arr, k):
        #arr:2차원 리스트
        #k: k번째 작은수
    answer = 0
    리스트=[ ]
    n=len(arr)
    #2차원 리스트를 1차원리스트로 변경
    for 세로 in range(n): #n은 배열의 세로길이
        for 가로 in range(4): # 4는 배열의 가로 길이
            리스트.append(리스트[세로][가로])
    #정력=>sort:오름차순 정렬하기
    리스트.sort()
    #k 번째 => 인덱스[k-1] 이유:인덱스는 0번부터 시작
    answer=리스트[k-1]
    return answer