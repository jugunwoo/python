#-*- coding: utf-8 -*-
import os
import sys
import urllib.request
import json



#-*- coding: utf-8 -*-
import os
import sys
import urllib.request
client_id ="As5wS7Sd6IWDNdNNKOpB"
client_secret ="Wy37zFFweX"
url = "https://openapi.naver.com/v1/datalab/shopping/categories";


body={"startDate":"2019-05-30",
      "endDate":"2021-05-30",
      "timeUnit":"date",
      "category":[{"name":"면세점","param":["50000010"]}],
      "device":"",
      "gender":"",
      "ages":[ ]
      }

body=json.dumps(body,ensure_ascii=False)

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
request.add_header("Content-Type","application/json")
response = urllib.request.urlopen(request, data=body.encode("utf-8"))
rescode = response.getcode()

if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)
