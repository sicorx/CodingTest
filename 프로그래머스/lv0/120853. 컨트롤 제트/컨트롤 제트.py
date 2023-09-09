def solution(s):
    answer = 0
    tmp = []
    
    tmp = s.split(' ')
    
    for i in range(len(tmp)) :
        if tmp[i] != 'Z' :
            answer += int(tmp[i])
        else :
            answer -= int(tmp[i-1])
    return answer