def solution(n_str):
    answer = ''
    i = 0
    for i in range(len(n_str)) :
        if n_str[i] != '0' :
            break
    answer = n_str[i:]
    print(answer)
    return answer