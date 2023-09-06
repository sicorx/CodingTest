def solution(str1, str2):
    answer = 0
    
    tmp = str2.find(str1)
    if tmp >= 0 :
        answer = 1
    
    return answer