# 두 정수 사이의 합 
# https://school.programmers.co.kr/learn/courses/30/lessons/12912 
# 주요 개념 : list(range(a, b+1)) 

def solution(a, b):
    if a < b :
        return sum(list(range(a, b+1)))
    else:
        return sum(list(range(b, a+1)))
    return answer 

# 개인 문제 풀이 과정
# https://kitsch2023.tistory.com/186 
