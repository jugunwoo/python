#변수는 저장 공간
    #num=10
#리스트는 여러개의 변수를 저장하는 공간
    #list=[변수1,변수2,변수3~~]


#문제51 여러개 변수를 저장하는 공간 [] 안에 변수 넣기
movie_rank=["닥터 스트레인지","스플릿","럭키"]
print(movie_rank)

#문제52
movie_rank=["닥터 스트레인지","스플릿","럭키"]
movie_rank.append("배트맨")
print(movie_rank)

#문제53. 리스트명.insert(인덱스번호,추가할변수)
movie_rank=["닥터 스트레인지","스플릿","럭키"]
movie_rank.insert(1,"슈퍼맨")
print(movie_rank)

#문제54
movie_rank=["닥터 스트레인지","슈퍼맨","스플릿","럭키","배트맨"]
movie_rank.remove("럭키")
print(movie_rank)

#문제55.
movie_rank=["닥터 스트레인지","슈퍼맨","스플릿","배트맨"]
del movie_rank[2]#스플릿 삭제=>배트맨=>스플릿 자리로 이동
del movie_rank[2]#배트맨 삭제
print(movie_rank)


#문제56.
lang1=["C","C++","JAVA"]
lang2=["python","GO","C#"]
리스트=lang1+lang2
print(리스트)

#문제57.
nums=[1,2,3,4,5,6,7]
print(max(nums))
print(min(nums))

#문제58.
nums=[1,2,3,4,5]
print(sum(nums))

#문제59.
cook=["피자","김밥","만두","양념치킨","족발","피자","김치만두","쫄면","쏘세지","라면","팥빙수","김치전"]
print(len(cook))

#문제60.
nums=[1,2,3,4,5]
print(sum(nums)/len(nums))

#문제61.
