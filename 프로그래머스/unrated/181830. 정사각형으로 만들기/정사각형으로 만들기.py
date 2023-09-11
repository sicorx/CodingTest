def solution(arr):
    answer = [[]]
    cnt = len(arr)
    
    for i in range(len(arr)) :
        if cnt < len(arr[i]) : 
            cnt = len(arr[i])
    
    if cnt > len(arr) :
        arr += [[0]] * (cnt - len(arr))
        
    
    for i in range(len(arr)) :
        if cnt > len(arr[i]) :
            arr[i] += [0] * (cnt - len(arr[i]))
            
    answer = arr
    return answer