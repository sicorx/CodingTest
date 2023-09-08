def solution(arr, idx):
    answer = 0
    arr = arr[idx:]
    
    if 1 in arr :
        answer = arr.index(1) + idx
    else :
        answer = -1
    return answer