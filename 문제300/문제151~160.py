#151.
리스트=[3,-20,-3,44]
for 변수 in 리스트:
    if 변수<0:
        print(변수)

#152.
리스트=[3,100,23,44]
for 변수 in 리스트:
    if 변수%3==0:
        print(변수)

#153.
리스트=[13,21,12,14,30,18]
for 변수 in 리스트:
    if 변수<20 and 변수%3==0:
        print(변수)

#154.
리스트=["I","study","python","language","!"]
for 변수 in 리스트[1:4:1]:
    print(변수)

#155.
리스트=["A","b","c","D"]
for 변수 in 리스트:
    if 변수.isupper():
        print(변수)

#156.
리스트=["A","b","c","D"]
for 변수 in 리스트:
    if 변수.islower():
        print(변수)

#157.
리스트=["dog","cat","parrot"]
for 변수 in 리스트:
    print(변수.upper())

#158.
리스트=["hello.py","ex01.py","intro.hwp"]
for 변수 in 리스트:
    a=변수.split(".")
    print(a[0])

#159.
리스트=["intra.h","intra.c","define.h","run.py"]
for 변수 in 리스트:
    b=변수.split(".")
    if b[1]=="h":
        print(변수)

#160.
리스트=["intra.h","intra.c","define.h","run.py"]
for 변수 in 리스트:
    b=변수.split(".")
    if b[1]=="h" or b[1]=="c":
        print(변수)