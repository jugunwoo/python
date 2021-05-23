#1.
def solution(shirt_size): #함수 만들기
    #지문보고 문제 풀기
    size_count=[0,0,0,0,0,0]

    for ss in shirt_size: #리스트 반복=>리스트내 항목이 변수에 하나씩 대입
        if ss=="XS":
            size_count[0] +=1
        if ss=="S":
            size_count[1] +=1
        if ss=="M":
            size_count[2] +=1
        if ss=="L":
            size_count[3] +=1
        if ss=="XL":
            size_count[4] +=1
        if ss=="XXL":
            size_count[5] +=1
    return size_count

    #함수가 끝나면서 돌려주는 값=> return=>리스트를 리턴
shirt_size=["XS","S","L","L","XL","S"]
ret=solution(shirt_size) #함수 불러내기

print("solution:return value of the function is",ret,".")





