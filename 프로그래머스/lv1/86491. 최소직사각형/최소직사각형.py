def solution(sizes):
    answer = 0
    
    for i in range(len(sizes)) :
        sizes[i] = list(sorted(sizes[i]))
        print(sizes[i])
    
    
    x = 0
    y = 0
    
    for i in range(len(sizes)) :
        if x < sizes[i][0] :
            x = sizes[i][0]
            
        if y < sizes[i][1] :
            y = sizes[i][1]
        
    answer = x * y
    return answer