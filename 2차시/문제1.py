#2차시
#문제1. 제품의 제품번호를 count[제품번호] +=1 추가

max_product_number=10
def func_a(gloves):
    #각 제품별 0으로 설정 해서 리스트 만들기
    counter=[0 for _ in range(max_product_number+1)]
    # counter=[0,0,0,0,0,0,0,0,0,0]
    for x in gloves:#해당 장갑의 제품번호=인덱스 번호
        counter[x] +=1
    return counter

def solution(left_gloves,right_gloves):
    left_counter=func_a(left_gloves)#왼손 장갑 제품별 개수 세기
    right_counter=func_a(right_gloves)#오른손 장갑 제품별 개수 세기

    total=0
    for i in range(1,max_product_number+1):
        total += min(left_counter[i],right_counter[i])
    return total

left_gloves=[2,1,2,2,4]#왼손 장갑에 제품번호
right_gloves=[1,2,2,4,4,7]#오른손 장갑의 제품번호
ret=solution(left_gloves,right_gloves)
print("solution 함수의 반환 값은",ret,"입니다.")