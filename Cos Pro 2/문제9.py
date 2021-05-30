

#문제9
def solution(characters):
    result="" #공백
    result += characters[0] # 첫문자 문자를 result 저장
    for i in range(1,len(characters)):#하나씩 비교
            #0[첫번째]제외한 1[두번째]부터 비교
        if characters[i-1] != characters[i]:
            result +=characters[i]
                #첫문자를 또 저장하면 오류
    return result

characters="senteeeencccccceeee" # => sentence 구하기
ret=solution(characters)
print("solution 함수 결과",ret)