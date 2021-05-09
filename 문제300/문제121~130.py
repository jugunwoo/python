# 121.
소대 = input("입력:")
if 소대.islower():
    print(소대.upper())
else:
    print(소대.lower())

# 122.
score = int(input("점수 입력:"))
if 81 <= score <= 100:
    print("grade is A")
elif 61 <= score <= 80:
    print("grade is B")
elif 41 <= score <= 60:
    print("grade is C")
elif 21 <= score <= 40:
    print("grade is D")
else:
    print("grade is E")

# 123.
환율={"달러":1167,"엔":1.096,"유로":1268,"위안":171}
입력저장=input("금액과 통화명 입력:")
금액,통화명=입력저장.split(" ")#공백 기준으로 분리
print(int(금액)*환율[통화명],"원")#환율 딕셔너리에서 입력한 통화명 찾아서 값 가져오기


#124.#max():가장 큰거 찾아내기
숫자1=int(input("입력:"))
숫자2=int(input("입력:"))
숫자3=int(input("입력:"))
print(max(숫자1,숫자2,숫자3))


#125.
번호=input("전화 번호 입력:")
앞번호=번호.split("-")[0]
if 앞번호=="011":
    print("SKT 사용자 입니다.")
elif 앞번호=="016":
    print("KT 사용자 입니다.")
elif 앞번호=="019":
    print("LGU 사용자 입니다.")
else:
    print("알수없음")

#126.
우편번호=input("입력:")
우편번호=우편번호[0:3]#0~2까지 까져오기
if 우편번호 in ["010","011","012"]: #010 011 012:강북구 번호가 포함되어 있으면
    print("강북구")
elif 우편번호 in ["014","015","016"]: # 014 015 016:도붕구 번호가 포함되어 있으면
    print("도봉구")
else:
    print("노원구")
#127.
주민등록번호=input("입력:")
주민=주민등록번호.split("-")[1][0]
if 주민==1 or 3:
    print("남자")
else:
    print("여자")

#128.
주민등록번호=input("입력:")
자리=주민등록번호.split("-")[1]
if 0<= int(자리[1:3])<=8:
    print("서울 입니다.")
else:
    print("서울이 아닙니다")

#129.
주민번호=input("주민등록번호 입력:")
계산1=int(주민번호[0])*2+int(주민번호[1])*3+int(주민번호[2])*4+int(주민번호[3])*5+int(주민번호[4])*6+\
      int(주민번호[5])*7+int(주민번호[7])*8+int(주민번호[8])*9+int(주민번호[9])*2+int(주민번호[10])*3+\
      int(주민번호[11])*4+int(주민번호[12])*5
계산2=11-(계산1&11)
계산3=str(계산2)
if 주민번호[-1]==계산3[-1]:#주민번호 마지막 번호 와 계산후 값의 마지막변화가 같으면
    print("유효한 주민등록번호 입니다.")
else:
    print("유효하지 않는 주민등록번호 입니다.")

#130.
import requests
btc=requests.get("https://api.bithumb.com/public/ticker/").json()['data']
변동폭=float(btc['max_price'])-float(btc['main_price'])
시가=float(btc['opening_price'])
최고가=float(btc['max_price'])

if (시가+변동폭)>최고가:
    print("상승장")
else:
    print("하락장")