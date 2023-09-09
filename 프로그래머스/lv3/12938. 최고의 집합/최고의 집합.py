import itertools
def solution(n, s):
    answer = []
    
    if s < n :
        answer.append(-1)
        return answer
    
    while n >= 1 :
        answer.append(s // n)
        s -= s // n
        n -= 1
    return answer