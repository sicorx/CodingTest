def solution(n):
    answer = 0
    
    cuzz = 0
    
    for i in range(1, n+1) :
        
        cuzz += 1
        while cuzz % 3 == 0 or '3' in str(cuzz) :
            cuzz += 1
        #print(i,':', cuzz)
    
    answer = cuzz
    return answer