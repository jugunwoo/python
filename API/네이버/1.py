#네이버 검색 api 이용한 json 가공 프로그램
import urllib.request
import json
import re


def 네이버검색(카테고리,검색결과수):
    클라이언트id = "As5wS7Sd6IWDNdNNKOpB"
    클라이언트secret = "Wy37zFFweX"
    client_id = 클라이언트id
    client_secret = 클라이언트secret
    #검색결과를 json 으로 가져오기
    url="https://openapi.naver.com/v1/search/"+카테고리+".json"
    option="&display="+검색결과수+"&sort=count" #display:출려갯수 : 검색결과 수
    query="?query="+urllib.parse.quote(input(카테고리+"의 검색 정보 입력:"))
    url_query=url+query+option

    request=urllib.request.Request(url_query)
    request.add_header("X-Naver-client-ID",client_id)
    request.add_header("X-Naver-client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read()
    else:
        print("Error Code:" + rescode)

    검색결과=response_body.decode('utf-8')#utf-8:한글 지원
    #검색결과 가공하기
    json결과=json.loads(검색결과)
    for i in json결과['items']:
        타이틀 = re.sub('<.+?>', '', i['title'], 0, re.I | re.S)
        print("---->검색결과:"+타이틀) #엔터 위에 원화기호 특수문자 :시프트 +\

        if 카테고리 =="shop":
            print("------->최저가:",i['lprice'])
        if 카테고리=="movie":
            print(("------>평점:",))



while True:
    print("검색[naverAPI]프로그램")
    print("카테고리[1.뉴스 2.쇼핑 3.도서]0.종료")
    선택=int(input("선택:"))#입력받아 선택변수에 저장
    #선택 제어
    if 선택==1:
        카테고리="news"
        검색결과수=input("-->뉴스 선택 했습니다. 몇개 출력할까요?")
        네이버검색(카테고리,검색결과수) #함수 불러내기
    if 선택==2:
        카테고리="shop"
        검색결과수=input("-->쇼핑 선택 했습니다. 몇개 출력할까요?")
        네이버검색(카테고리, 검색결과수)
    if 선택==3:
        카테고리 = "book"
        검색결과수 = input("-->도서 선택 했습니다. 몇개 출력할까요?")
        네이버검색(카테고리, 검색결과수)
    if 선택==4:
        카테고리="movie"
        검색결과수 = input("-->영화 선택 했습니다. 몇개 출력할까요?")
        네이버검색(카테고리, 검색결과수)