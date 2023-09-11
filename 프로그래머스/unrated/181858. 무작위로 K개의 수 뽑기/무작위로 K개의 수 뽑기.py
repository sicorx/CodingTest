def solution(arr, k):
    answer = []
    
    for i in arr :
        if i in answer :
            pass
        else :
            answer.append(i)
        
        if len(answer) == k :
            break
    if len(answer) != k :
        answer += [-1] * (k - len(answer))
    return answer