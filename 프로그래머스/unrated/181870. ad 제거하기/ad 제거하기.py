def solution(strArr):
    answer = []
    
    for i in strArr :
        if i.find('ad') < 0 :
            answer.append(i)
    return answer