def solution(arr):
    answer = []
    tmp = 0
    for i in range(len(arr)) :
        
        if arr[i] >= 50 and arr[i] % 2 == 0 :
            tmp = arr[i] / 2
        elif arr[i] < 50 and arr[i] % 2 == 1 :
            tmp = arr[i] * 2
        else :
            tmp = arr[i]
        answer.append(tmp)
        
    return answer