
# 현재 금 가격 크롤링
from bs4 import BeautifulSoup as bs
import urllib.request as ur

주소='https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%ED%98%84%EC%9E%AC+%EA%B8%88+%EA%B0%80%EA%B2%A9&oquery=k3&tqi=h7cy%2Bwp0J14sstR067ossssst%2Bh-126727'
웹문서=ur.urlopen(주소)
soup=bs(웹문서.read(),'html.parser')
태그=soup.find_all('em',{"class":"down _now_value"})
print("현재 금의 가격은:"+태그[0].text)