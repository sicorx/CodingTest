def solution(s):
    answer = ''
    tmp = []
    mi = 0
    ma = 0
    
    tmp = s.split(' ')
    
    for i in range(len(tmp)) :
        tmp[i] = int(tmp[i])
    mi = min(tmp)
    ma = max(tmp)
    
    answer = str(mi) + ' ' + str(ma)
    return answer