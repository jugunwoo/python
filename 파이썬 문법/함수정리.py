#함수정리
#6.split() 함수
#정의:리스트를 만들어주는 함수
#사용방법:문자열.split()


#10.strip() rstirp() lstrip()
#정의:strip() : 양쪽 공백 제거   rstrip() : 오른쪽 공백 제거  lstrip(): 왼쪽 공백 제거
#사용방법:data = "   039490    "
#print(data.rsplit())

#11.upper() lower() capitalize() 함수
#정의:upper()함수:대문자로 변환 해주는 함수  lower() 함수 : 소문자로 변환 해주는 함수  capitalize() 함수 : 첫글자만 대문자로 변환 해주는 함수
#사용방법:print(ticker.upper())   print(ticker.lower())   print(ticker.capitalize())

#12.endswith()  startswith() 함수
#정의:  endswith() 함수 : 끝냐는 문자가 맞는지 확인 함수  startswith() 함수 : 시작하는 문자가 맞는지 확인 함수
#사용방법:print(file_name.endswith( ("xlsx","xls")) )    print(file_name.startswith("2020"))

#13.리스트와 변수 차이
#변수는 1가지 값밖에 저장하지 못하지만 리스트는 한번에 여러개 가능하다

#14.append() insert() del 함수
#정의:append():리스트에 변수 추가  insert():인덱스에 변수를 추가   del: 리스트에 있는 변수 삭제
#사용방법: 리스트명.append(변수)    리스트명.insert(인덱스번호,추가할변수)  del 리스트명[인덱스번호]


#15.max()  min()  sum()  len() 함수
#정의: max():리스트의 최고값  min():리스트의 최소값  sum():리스트의 변수의 합  len():리스트의 변수의 개수
#사용방법:  pirnt(max(리스트명))  print(min(리스트명))  print(sum(리스트명))  print(len(리스트명))