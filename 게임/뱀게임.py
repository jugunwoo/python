import pygame  #파이게임 파일 불러오기
from pygame.locals import QUIT,Rect,KEYDOWN,K_UP,K_LEFT,K_RIGHT,K_DOWN
                        #종류 , 직각 , 키 눌렀을때 , 위방향키 ,왼쪽 방향키 ,오른쪽 방향키 , 아래방향키
import random #랜덤파일 불러오기
import sys #시스템 파일 불러오기

#2.게임에 필요한 기본설정
pygame.init() #파이게임 초기값
화면=pygame.display.set_mode((1000,1000))
프레임=pygame.time.Clock() #시간 체크
#Frame Per second: FPS : 초당 프레임수

음식=[] #여러개 음식을 저장할 리스트
뱀=[] # 여러개 뱀 꼬리를 저장할 리스트
(가로,세로)=(50,50) #가로길이 세로길이


#배경넣기
배경=pygame.image.load("물_배경.png.jpg")

#배경소리넣기
pygame.mixer.music.load("background-loop-melodic-techno-03-2691.mp3")
pygame.mixer.music.play(-1)

#3.함수 만들기
    #1.음식함수 2.음식 이동함수 3.그리기함수
#1
def 음식생성(): #어딘가에 음식을 배치하는 함수를 선언
    while True:#무한반복
        위치=(random.randint(0,가로-1),random.randint(0,세로-1))
        if 위치 in 음식 or 위치 in 뱀:#해당위치에 음식이나 뱀이 있으면
            continue#다시 실행
        else:#해당 위치에 음식이나 뱀이 없으면
            음식.append(위치)#음식리스트에 해당위치 추가
            break
#2
def 음식이동(위치):
    임의변수=음식.index(위치)#index:해당 위치에 음식 찾기
    del 음식[임의변수]#해당 위치에 음식 삭제
    음식생성()#음식생성 함수 호출[새로운 음식 생성]

#3
def 그리기(점수판,게임종료메세지):



    #음식 그리기
    for food in 음식:
        pygame.draw.ellipse(화면,(0,255,0),Rect(food[0]*20,food[1]*20,20,20))
    #뱀 그리기                #타원그리기(화면이동,칼라,터원(x축 , y축 , 가로크기 , 세로크기))
    for body in 뱀:#리스트내 갯수만큼 반복
        pygame.draw.rect(화면,(0,255,255),Rect(body[0]*20,body[1]*20,20,20))
                    #사각형그리기(화면이동,칼라,사각형(x축 , y축 ,가로크기,세로크기))
    pygame.display.update()#화면 업데이트

    #점수 그리기
    if 점수판 !=None: #점수에 내용이 있으면
        화면.blit(점수판,(10,10)) # x좌표 y좌표에 표기


    #종료 메세지 그리기
    if 게임종료: #게임종료메세지 내용이 있으면
        게임종료메세지 = my글꼴.render("게임종료[획득점수는:" + str(점수)+"]", True, (255, 255, 0))
        화면.blit(게임종료메세지,(300,500))

    pygame.display.update()

#4.게임실행
my글꼴=pygame.font.SysFont("malgungothic",30)
키=K_DOWN#아래키
게임종료=False #게임종료 스위치
뱀.append((int(세로/2),int(가로/2))) # 뱀을 화면에 가운데 위치
점수=0


for i in range(30): #30개의 음식 생성
    음식생성()

while True: #계속 반복하기
    화면.blit(배경,(0,0))

    #키보드 동작하기
    for 동작 in pygame.event.get(): #파이게임 이벤트 있을경우
        if 동작.type==QUIT: #이벤트가 종료이면
            pygame.quit() # 파이게임 종료
            sys.exit() #시스템 종료
        elif 동작.type==KEYDOWN: #키를 눌렀을떄
            키=동작.key

    #키를 눌렀을때
    if not 게임종료: #게임종료가 False 이면
        if 키 == K_LEFT:
            머리=(뱀[0][0]-1,뱀[0][1])
        elif 키 ==K_RIGHT:
            머리=(뱀[0][0]+1,뱀[0][1])
        elif 키 == K_UP:
            머리=(뱀[0][0],뱀[0][1]-1)
        elif 키 == K_DOWN:
            머리=(뱀[0][0],뱀[0][1]+1)

        #뱀 몸에 닿았을때 혹은 화면 밖으로 나갔을때 게임종료
        if 머리 in 뱀 or 머리[0]<0 or 머리[0]>=세로 or 머리[1]<0 or 머리[1]>=가로:
            게임종료메세지 = my글꼴.render("게임종료 [획득점수는:" + str(점수)+"]", True, (255, 255, 0))
            게임종료=True


        #뱀 머리 추가
        뱀.insert(0,머리)

        #음식을 먹었을떄 꼬리 추가 아니면 추가 엑스
        if 머리 in 음식: # 만약에 머리가 음식에 닿았을떄
            음식이동(머리)#새로운 음식 추가
            #1점추가
            점수+=1
        else:
            뱀.pop() # 리스트내 가장 뒤에있는 항목 제거

        게임종료메세지 = my글꼴.render(" " + str(점수), True, (255, 255, 0))
        점수판=my글꼴.render("현재 먹은 횟수:"+str(점수),True,(255,255,0))




    그리기(점수판,게임종료메세지)
    프레임.tick(5)