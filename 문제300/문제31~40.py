

#문제31
#31.
#예상
#7

#32.
#예상
#HiHiHI

#33.
print("-"*80)

#34.:문자열 곱하기
t1 = "python"
t2 = "java"
t3=t1=" "+t2 + " " #문자끼리 +로 연결
print(t3*4) #문자 반복*사용

#35.format : 형식[꾸미기] formatting : %
        # %s : 문자 형식  , %d :정수 형식
name1="김민수"
age1=10
name2="이철희"
age2=13
#이름: 김민수 나이: 10
#이름: 이철희 나이: 13
print("이름:%s 나이 : %d " %(name1,age1) )
print("이름:%s 나이 : %d " %(name2,age2) )

#36.format() 함수 사용
    # {} 안에 들어갈 데이터를 format 함수 안에 넣기
name1="김민수"
age1=10
name2="이철희"
age2=13
print("이름 : {} 나이 {}".format(name1,age1))
print("이름 : {} 나이 {}".format(name2,age2))

#37.:f-string
name1="김민수"
age1=10
name2="이철희"
age2=13
print(f"이름 : {name1} 나이 : {age1}")
print(f"이름 : {name2} 나이 : {age2}")

#38.
상장주식수="5,969,782,550"
컴마제거 = 상장주식수.replace(",","")
타입변환=int(컴마제거)
print(타입변환)
#39
분기="2020/03(E)  (IFRS연결)"
print(분기[0:7])
#she.
