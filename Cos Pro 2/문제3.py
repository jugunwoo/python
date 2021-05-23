
#문제3.
def func_a(month,day):
    #각 월의 일수[마지막날]
    month_list=[31,28,31,30,31,30,31,31,30,31,30,31]
    total=0;
    for i in range(month-1): #월-1 만큼 반복하기
        total +=month_list[i]
        #입력한 월의 전 월까지의 일수를 다 더하기
    total +=day #내가 입력한 월의 일수 더하기
        #총 1월 1일부터 내가 입력한 날짜까지의 임무를 구하기
    return total -1#하루 제외

def solution(start_month,start_day,end_month,end_day):
    start_total=func_a(start_month,start_day)
    end_total=func_a(end_month,end_day)
    return  end_total - start_total

start_month=1 #시작날짜의 월
start_day=2 #시작날짜의 일
end_month=2#끝나는 날짜의 월
end_day=2 #끝나는 날짜의 일
ret=solution(start_month,start_day,end_month,end_day)

print("solution:return value of the function is",ret,".")