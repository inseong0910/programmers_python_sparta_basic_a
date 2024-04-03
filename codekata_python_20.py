# 정수 내림차순으로 배치하기
# https://school.programmers.co.kr/learn/courses/30/lessons/12933 
# 주요 개념 : 리스트로 변환, 객체 정렬, 하나로 붙이기(join)

def solution(n):
    answer = 0
    abc = list(str(int(n)))
    abc.sort(reverse=True)
    return int("".join(abc)) 

# 개인 문제풀이 과정 : https://kitsch2023.tistory.com/175 
