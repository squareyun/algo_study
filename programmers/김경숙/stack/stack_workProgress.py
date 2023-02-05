import math


def solution(progresses, speeds):
    answer = []
    left = []
    cnt = 0

    for i in range(len(progresses)):
        left.append(math.ceil((100 - progresses[i]) / speeds[i]))

    max = left[0]
    for l in left:
        if max < l:
            answer.append(cnt)
            max = l
            cnt = 0

        cnt += 1

    answer.append(cnt)
    return answer

# print(solution([1, 1, 50], [100, 2, 1]))
