def solution(price, money):
    answer = money-sum(price)#sum(리스트) : 리스트의 합
    if answer<0:
        answer=-1
    return answer