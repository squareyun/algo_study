#link: https://school.programmers.co.kr/learn/courses/30/lessons/42586
#level: 2
#date: 20220204
#tag: implementation
#author: 윤우혁

def solution(progresses, speeds):
    answer = []
    length = len(progresses)
    
    idx = 0
    while sum(answer) != length:
        for i in range(idx, length):
            progresses[i] += speeds[i]
            
        if progresses[idx] >= 100:
            cnt = 0
            for j in range(idx, length):
                if progresses[j] >= 100:
                    cnt += 1
                else:
                    break
            answer.append(cnt)
            idx += cnt          
    
    return answer