# 정수 제곱근 판별 
# https://school.programmers.co.kr/learn/courses/30/lessons/12934 
# 주요 개념 : n이 양의 정수 x의 제곱이라면 ==> x는 n의 1/2제곱이다. 이렇게 뒤집어서 생각하는 방법도 있다.

def solution(n):
    answer = 0
    
    x = n**(1/2)
    if (x%1 == 0):
        answer = (x+1)**2
    else:
        answer = -1
    return answer 

# 개인 문제풀이 과정 : https://kitsch2023.tistory.com/172 
