#link: https://school.programmers.co.kr/learn/courses/30/lessons/12906
#level: 1
#date: 20220204
#tag: stack
#author: 윤우혁

def solution(arr):
    answer = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] == answer[-1]:
            continue
        answer.append(arr[i])
    return answer