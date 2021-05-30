import pygame
import sys
from pygame.locals import *

점수=0
게임종료=0
배경=pygame.image.load("벽돌사진.jpg")
pygame.init()
화면=pygame.display.set_mode((480,640))
pygame.display.set_caption("벽돌깨기게임")
시간=pygame.time.Clock()
pygame.key.set_repeat(1,1)

#벽돌 만들기

def 벽돌만들기():
    for 벽돌 in 벽돌리스트:
        pygame.draw.rect(화면,(211,149,0),벽돌)

def 공():
    pygame.draw.circle(화면,(255,255,0),(int(x),int(y)),10)

x=int(480/2)
y=640-30
dx=11
dy=-11
세로=10
가로=75
막대x=(480-가로)/2
막대=pygame.Rect(막대x,640-세로-10,가로,세로)

벽돌리스트=[]
for 열 in range(6):
    for 행 in range(10):
        벽돌=pygame.Rect(열*(60+10)+35,행*(16+5)+24,60,16)
        벽돌리스트.append(벽돌)
def 페달그리기():
    pygame.draw.rect(화면,(0,211,149),막대)

while True:
    화면.blit(배경,(0,0))
    if 게임종료==0:
        x+=dx #오른쪽 이동
        y+=dy #왼쪽 이동
    if x +dx>480-7 or x+dx<7:
        dx=-dx
    if y +dy<7:
        dy=-dy
    elif(y+dy>620):
        if x>막대x and x<막대x +가로:
            dy=-dy
        else:
            게임종료=1
    for 벽돌 in 벽돌리스트:
        if x>벽돌.x and x<벽돌.x+벽돌.width and y> 벽돌.y and y< 벽돌.y+벽돌.height:
            dy=-dy
            벽돌리스트.remove(벽돌)
            점수+=1

    for 동작 in pygame.event.get():
        if 동작.type==QUIT:
            pygame.quit()

        elif 동작.type==pygame.KEYDOWN:
            if 동작.key==pygame.K_LEFT:
                막대.left -=1
                막대x-=1
            elif 동작.key==pygame.K_RIGHT:
                막대.right+=1
                막대x+=1
    벽돌만들기()
    공()
    페달그리기()

    if 게임종료==1:
        글꼴1=pygame.font.SysFont("malgungothic",32)
        점수메세지=글꼴1.render("게임종료"+str(점수),True,(0,255,0))
        화면.blit(점수메세지,(165,300))
    pygame.display.update()
    시간.tick(30)

