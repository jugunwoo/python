def solution(attack,recovery,hp):
    count=0 #공격 횟수
    while(True):
        count +=1 #공격횟수 1증가
        hp -=attack #몬스터체력 -=공격력
        if hp <=0:#만약에 몬스터 체력<0이면
            break
        hp+=recovery #몬스터체력 +=회복력
    return count

attack=30 #캐릭터 공격력
recovery=10 #몬스터의 회복체력
hp=60 #몬스터의 초기체력
ret=solution(attack,recovery,hp)

print("solution 함수 반환 값은",ret,"입니다.")

#몬스터 60
#count=1    #공격 -30 =>몬스터 30
            #회복 +10 =>몬스터 40

#count=2
            #공격 -30 =>몬스터 10
            #회복 +10 =>몬스터 20

#count=3    #공격 -30 =>몬스터 -10