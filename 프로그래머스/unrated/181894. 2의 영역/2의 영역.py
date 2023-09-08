def solution(arr):
    answer = []
    
    if 2 in arr :
        s = arr.index(2)
        e = len(arr) - list(reversed(arr)).index(2)
        answer = arr[s:e]
        
    else :
        answer.append(-1)
    return answer