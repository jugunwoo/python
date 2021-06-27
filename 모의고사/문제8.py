def solution(name_list):
    answer = 0 #이름에 j,k 포함되어 있는 학생수
    for name in name_list: #학생목록에 하나씩 name에 대입
        for n in name: # name에 문자 하나씩 n에 대입
            if n == 'j' or n == 'k':
                answer += 1
                #continue 가장 가까운 반복문으로 이동(for 다시 실행)
                break #가장 가까운 for 종료
    return answer