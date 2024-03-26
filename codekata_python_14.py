# 약수의 합
# https://school.programmers.co.kr/learn/courses/30/lessons/12928 
# 주요 개념 : 약수는 어떤 정수를 나누었을 때 나머지가 0이 되는 수

def solution(n):
    answer = 0
    for i in range(1, n+1):
        if (n%i == 0):
            answer += i
    return answer

# 개인 문제풀이 과정 
# https://kitsch2023.tistory.com/158 
# 비고 : 어려웠던 문제 
