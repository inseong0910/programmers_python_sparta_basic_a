# 나머지가 1이 되는 수 찾기
# https://school.programmers.co.kr/learn/courses/30/lessons/87389 
# 주요 개념 : for ~ break 

def solution(n):
    for i in range(1, n):
        if n%i == 1:
            answer = i
            break
    return answer 

# 개인 문제풀이 과정 
# https://kitsch2023.tistory.com/159
