from bs4 import BeautifulSoup as bs
import urllib.request as ur
import urllib

지역=input("지역:")

주소='https://search.naver.com/search.naver?'
웹문서=ur.urlopen(주소)
soup=bs(웹문서.read(),'html.parser')
태그=soup.find_all('span',{"class":"todaytemp"})
print("현재 신촌의 날씨는:",태그[0].text+"도 입니다.")

#신촌날씨의 미세먼지 출력
미세먼지=soup.find_all('dd',{"class":"lv1"})
print("현재 신촌의 미세먼지:",미세먼지[0].text)

#신촌날씨의 오존지수 출력
오존지수=soup.find_all('dd',{"class":"lv2"})
print("현재 신촌의 오존지수는:",오존지수[0].text)