# 콜라츠 추측
# https://school.programmers.co.kr/learn/courses/30/lessons/12943 
# 주요 내용 : for 반복문 

def solution(num):
    for i in range(500):
        num = num / 2 if num % 2 == 0 else num*3 + 1
        if num == 1:
            return i + 1
    return -1 

# 개인 문제 풀이 과정 
# https://kitsch2023.tistory.com/188 
