
#41 upper()함수:대문자로 변환 해주는
ticker = "btc_krw"
print(ticker.upper())

#42. lower() 함수 : 소문자로 변환 해주는 함수
ticker = "btc_krw"
print(ticker.lower())

#43. capitalize() 함수 : 첫글자만 대문자로 변환 해주는 함수
ticker = "btn_krw"
print(ticker.capitalize())

#44 : endswith() 함수 : 끝냐는 문자가 맞는지 확인 필수!
file_name ="보고소.xlsx"
print(file_name.endswith("xlsx"))

#45.
file_name="보고서.xlsx"
print(file_name.endswith( ("xlsx","xls")) )

#46. startswith() 함수 : 시작하는 문자가 맞는지 확인 함수
file_name = "2020_보고서.xlsx"
print(file_name.startswith("2020"))

#47.
a="hello world"
print(a.split()) # 공백 기준으로 2개로 분리되어 리스트에 저장

#48.
ticker = "btc_krw"
print(ticker.split("_"))#_기준으로 분리되어 리스트에 저장

#49.
date = "20202-05-01"
print(date.split("_"))#_기준으로 분리되어 리스트에 저장

#50. strip() : 양쪽 공백 제거  # rstrip() : 오른쪽 공백 제거 # lstrip(): 왼쪽 공백 제거
data = "   039490    "
print(data.rsplit())