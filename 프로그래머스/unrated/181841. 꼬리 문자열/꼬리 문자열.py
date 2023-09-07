def solution(str_list, ex):
    answer = ''
    
    for i in range(len(str_list)) :
        # print(str_list[i].find(ex))
        if str_list[i].find(ex) < 0 :
            answer += str_list[i]
    return answer