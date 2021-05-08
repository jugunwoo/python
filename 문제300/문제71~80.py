#71. #my_variable 이름의 비어있는 튜플을 만들라
my_variable=( ) #튜플 생성

#72.#영화 제목을 movie_rank 이름의 튜플에 저장하라
movie_rank=("닥터 스트레인지","스플릿","럭키")

#73. # 숫자1이 저장된 튜플을 생성하라
my_tuple=( 1 )
print(type(my_tuple))#int 정수 #튜플이 아니다
my_tuple=(1, )#,추가
print(type(my_tuple)) #튜플로 생성

#74.
#t=(1,2,3)
#t[0]="a" # 0번째 순서의 값을 a로 변환
    #오류 발생 이유: 튜플은 값을 바꿀수가 없다

#75.
#t=1,2,3,4
#타입: 튜플

#76.
#t=("a","b","c")
    #튜플은 수정 엑스

#77.
interest=("삼성전자","LG전자","SK Hynix")
print(list(interest))
    #list(튜플):리스트로 변환

#78.
interest=["삼성전자","LG전자","SK Hynix"]
print(tuple(interest))
    #tuple(list):튜플로 변환

#79.
temp=("apple","banana","cake")
a,b,c=temp
print(a,b,c)
#예상:apple banana cake

#80.
data=tuple(range(2,100,2))
print(data)
