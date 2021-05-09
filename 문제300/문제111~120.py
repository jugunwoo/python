#111.
입력=input("입력:")
print(입력*2)

#112.
입력2=int(input("입력:"))
print(입력2+10)

#113.
입력2=int(input("입력:"))
if 입력2 %2==0:
    print("짝수")
else:
    print("홀수")

#114.
입력2=int(input("입력:"))
if 입력2+20>255:
    print(255)

#115.
입력2=int(input("입력:"))
if 입력2-20<0:
    print(0)
elif 입력2-20>255:
    print(255)
else:
    print(입력2-20)

#116.
입력2=input("현재 시간:")
if 입력2[-2: ]=="00":
    print("정각입니다.")
else:
    print("정각이 아닙니다.")

#117.
fruit=["사과","포도","홍시"]
과일=input("좋아하는 과일은?:")
if 과일 in fruit:
    print("정답입니다.")

#118.
warn_investment_list=["Microsoft","Google","Naver","Kakao","SAMSUNG","LG"]
투자=input("투자 종목 입력:")
if 투자 in warn_investment_list:
    print("투자 경고 종목입니다.")
else:
    print("투자 경고 종목이 아닙니다.")

#119.
fruit={"봄":"딸기","여름":"토마토","가을":"사과"}
계절=input("좋아하는 계절은:")
if 계절 in fruit:
    print("정답입니다")
else:
    print("오답입니다.")

#120.
fruit={"봄":"딸기","여름":"토마토","가을":"사과"}
과일=input("좋아하는 과일은?:")
if 과일 in fruit:
    print("정답입니다.")
else:
    print("오답입니다.")