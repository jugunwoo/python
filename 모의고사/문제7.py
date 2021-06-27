#https://programmers.co.kr/learn/courses/33
def solution(s):
    s_lst = list(s)
    n = len(s) #n=문자열 개수
    for i in range(n): #문자열 개수 반복
        if s_lst[i] == 'a': #만약에 리스트에[i]=='a'이면
            s_lst[i] = 'z' #z로 변경
        elif s_lst[i]=='z':
            s_lst[i] =  'a' #만약에 리스트에[i] =='z'이면
    return "".join(s_lst)#a로 변경

#첫번째 IF가 T이더라도 두번째 IF도 검사 실행
#if 조건1:
#if 조건2:

#첫번째 if 가 T이면 두번재 elif는 검사 안함
#if 조건1:
#elif 조건2:
