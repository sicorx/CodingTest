def solution(myString, pat):
    answer = 0
    
    for i in range(len(myString)) :
        if myString[i:].find(pat) == 0 :
            answer += 1
    return answer