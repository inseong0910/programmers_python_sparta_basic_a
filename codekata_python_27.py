# 핸드폰 번호 가리기
# https://school.programmers.co.kr/learn/courses/30/lessons/12948 
# 주요 개념 : 전화번호 뒤 4자리 => for i in rannge(len(phone_number)) < 4 

def solution(phone_number):
    answer = ''
    
    for i in range(len(phone_number)):
        if i < len(phone_number) - 4:
            answer += '*'
        else:
            answer += phone_number[i]
    return answer 

# 개인 문제 풀이
# https://kitsch2023.tistory.com/219 
