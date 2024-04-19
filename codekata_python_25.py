# 나누어 떨어지는 숫자 배열
# https://school.programmers.co.kr/learn/courses/30/lessons/12910

def solution(arr, divisor):
    answer = []
    
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
            
    if len(answer) == 0:
        answer.append(-1)

    answer.sort()
    return answer 

# 개인 문제 풀이 과정
# https://kitsch2023.tistory.com/197 
