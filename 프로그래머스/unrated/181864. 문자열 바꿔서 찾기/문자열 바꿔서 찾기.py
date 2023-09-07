def solution(myString, pat):
    answer = 0
    tmp = ''
    
    for i in range(len(pat)) :
        if pat[i] == 'A' :
            tmp += 'B'
        else :
            tmp += 'A'
    
    if myString.find(tmp) >= 0 :
        answer = 1
    
    return answer