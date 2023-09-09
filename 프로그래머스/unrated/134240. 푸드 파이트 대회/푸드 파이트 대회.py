def solution(food):
    answer = '0'
    
    seq = len(food) - 1
    
    for i in food[::-1] :
        answer += str(seq) * (i // 2)        
        answer = str(seq) * (i // 2) + answer
        seq -= 1
        
            
        
    return answer