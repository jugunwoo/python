#61.
import asyncio

price=['20180728,100,130,140,150,160,170']
print(price[1:])
    #[인덱싱] = [1: ] = 2번째값부터 끝까지
#62.
nums=[1,2,3,4,5,6,7,8,9,10]
print(nums[ : :2])
    #[인덱싱] = [ : : 2] = 0번째 값부터 끝까지 2개씩 이동=1 3 5 7 9
    #[시작번호:끝번호:이동단위]

#63.
nums=[1,2,3,4,5,6,7,8,9,10]
print(nums[1: :2])
    #[1: :2]=2부터 끝까지 2씩 이동=2 4 6 8 10

#64.
nums=[1,2,3,4,5]
print(nums[ : :-1])
    #[ : :-1]=뒤로 이동

#65.
interest=["삼성전자","LG전자","Naver"]
print(interest[0],interest[2])

#66.
interest=["삼성전자","LG전자","Naver","SK하이닉스","미래에셋대우"]
print(" ".join(interest))
    #join 함수: 리스트 내 항목을 합칠때 사용

#67."/".join(리스트)
interest=["삼성전자","LG전자","Naver","SK하이닉스","미래에셋대우"]
print("/".join(interest))

#68."\n".join(리스트)
interest=["삼성전자","LG전자","Naver","SK하이닉스","미래에셋대우"]
print("\n".join(interest))

#69.
string="삼성전자/LG전자/Naver"
interest=string.split("/")
print(interest)

#70.
data=[2,4,3,1,5,10,9]
data.sort()
print(data)
#내림차순
data.sort(reverse=True)
print(data)



