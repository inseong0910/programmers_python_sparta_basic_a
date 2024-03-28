# x만큼 간격이 있는 n개의 숫자
# https://school.programmers.co.kr/learn/courses/30/lessons/12954 
# 주요 개념 : for문, 빈 리스트 선언, append() 함수

def solution(x, n):
    answer = []
    for i in range(1, n+1):
        answer.append(x*i)
    return answer

# 개인 문제풀이 과정
# https://kitsch2023.tistory.com/163 
