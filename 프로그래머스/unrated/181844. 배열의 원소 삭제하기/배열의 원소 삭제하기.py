def solution(arr, delete_list):
    answer = []
    
    for i in range(len(delete_list)) :
        for j in range(len(arr)) :
            if arr[j] == delete_list[i] :
                arr.remove(delete_list[i])
                break
    answer = arr
            
    return answer