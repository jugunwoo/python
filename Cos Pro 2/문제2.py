
#문제2

def solution(price,grade): #함수(가격,등급) 인수를 받는다
    answer=0
    if grade=="S":
        answer=price*0.95 #1:100%   0.5:50%
    if grade=="G":
        answer=price*0.9
    if grade=="V":
        answer=price*0.85
    return int(answer)#계산된 가격을 리턴

price1=2500
grade1="V"
ret1=solution(price1,grade1) #함수 호출(가격,등급) 인수를

print("solution:return value of the function is",ret1,".")

price2=96900
grade2="S"
ret2=solution(price2,grade2)

print("solution:return value of the function is", ret2,".")

