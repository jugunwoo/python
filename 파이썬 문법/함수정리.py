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

#16.join 함수
#정의:리스트 내 항목을 합칠때 사용하는 함수
#사용방법:."/".join(리스트),"\n".join(리스트),print(" ".join(interest))

#17. \n,\t
#정의:\n :줄바꿈 \t:탭(띄어쓰기)
#사용방법:a=d\td pint(a),"\n".join(리스트)

#18.리스트를 오름차순/내림차순
#사용방법:
#오름차순
# data=[2,4,3,1,5,10,9]
#data.sort()
#print(data)
#내림차순
#data.sort(reverse=True)
#print(data)

#19.데이터를 저장하는방법 4가지 의 차이와 사용방법
#변수=a=[1,2,3]
#리스트=a=[1,2,3]
#튜플=movie_rank=("닥터 스트레인지","스플릿","럭키")
#딕셔너리=아이스크림={"메로나":1000,"폴라포":1200,"빵빠레":1800}

#20.튜플 리스트로 변환 방법
# #list(튜플):리스트로 변환


#21.리스트 튜플로 변환 방법
##tuple(list):튜플로 변환


#22.튜플 언팩킹 이란
#정의:튜플의 각 요소를 여러 개의 변수에 할당
#사용방법:a,b,c = 10,20,30
#print(a,b,c)

#23.딕셔너리 활용
#1.딕셔너리 리스트 추가하는 방법
#딕셔너리명["키"]=값
#2.딕셔너리 키 만 출력하는 방법
#list(딕셔너리.keys())
#3.딕셔너리의 값 만 출력하는 방법
#list(아이스크림.values())
#4.두 개의 딕셔너리를 합치는 방법
#딕셔너리명1.update(딕셔너리명2)
#5.[키] 튜플과 [값] 튜플을 딕셔너리 변환하는 방법
#dict(zip(튜플명,튜플명))
#5.[키] 리스트와 [값] 리스트를 딕셔너리 변환하는 방법
#dict(zip(리스트명,리스트명))