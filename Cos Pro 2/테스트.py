def solution(attack,recovery,hp):
    count=0
    while True:
        count+=1
        hp-=attack
        hp+=recovery
        if hp<=0:
            break
    return count

attack=30
recovery=10
hp=60
ret=solution(attack,recovery,hp)
print("횟수는",ret)