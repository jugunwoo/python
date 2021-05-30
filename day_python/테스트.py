
# 현재 금 가격 크롤링
from bs4 import BeautifulSoup as bs
import urllib.request as ur

주소='https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%ED%98%84%EC%9E%AC+%EA%B8%88+%EA%B0%80%EA%B2%A9&oquery=k3&tqi=h7cy%2Bwp0J14sstR067ossssst%2Bh-126727'
웹문서=ur.urlopen(주소)
soup=bs(웹문서.read(),'html.parser')
태그=soup.find_all('em',{"class":"down _now_value"})
print("현재 금의 가격은:"+태그[0].text)



#API

import urllib.request
import json
import re


def 네이버검색(카테고리):
    클라이언트id = "As5wS7Sd6IWDNdNNKOpB"
    클라이언트secret = "Wy37zFFweX"
    client_id = 클라이언트id
    client_secret = 클라이언트secret
    #검색결과를 json 으로 가져오기
    url="https://openapi.naver.com/v1/search/"+카테고리+".json"
    option="&display="+"&sort=count" #display:출려갯수 : 검색결과 수
    query="?query="+urllib.parse.quote(input(" 검색 정보 입력:"))
    url_query=url+query+option

    request = urllib.request.Request(url_query)
    request.add_header("X-Naver-client-ID", client_id)
    request.add_header("X-Naver-client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read()
    else:
        print("Error Code:" + rescode)

        검색결과 = response_body.decode('utf-8')
        json결과=json.loads(검색결과)
        for i in json결과['items']:
            타이틀=re.sub('<.+?>','',i['title'],0,re.I | re.S)
            print()