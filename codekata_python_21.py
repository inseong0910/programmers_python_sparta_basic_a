# 하샤드 수
# https://school.programmers.co.kr/learn/courses/30/lessons/12947
# 주요 개념 : for i , sum+= 

def solution(x):
    sum = 0
    for i in str(x):
        sum += int(i)
    
    if x % sum == 0:
        return True
    return False 

# 개인 문제 풀이 과정 
# https://kitsch2023.tistory.com/182 
