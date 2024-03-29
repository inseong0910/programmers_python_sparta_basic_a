# 자연수 뒤집어 배열로 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/12932 
# 주요 내용 : 리스트, 슬라이싱, 역방향은 -1 

def solution(n):
    n = str(n)
    answer = []
    
    for i in n:
        answer.append(int(i))
        
    answer = answer[::-1]
    return answer 

# 개인 문제풀이 과정
# https://kitsch2023.tistory.com/165
