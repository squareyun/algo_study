from collections import deque


def solution(priorities, location):
    answer = 1
    enum_prior = deque(enumerate(priorities))

    while enum_prior:
        max_p = max(enum_prior, key=lambda x: x[1])[1]
        tmp = enum_prior.popleft()
        if tmp[0] == location and tmp[1] == max_p:
            return answer
        elif tmp[1] < max_p:
            enum_prior.append(tmp)
        else:
            answer += 1
