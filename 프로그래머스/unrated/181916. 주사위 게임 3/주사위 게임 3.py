def solution(a, b, c, d):
    answer = 0
    s = set([a, b, c, d])
    nums = [a, b, c, d]
    counts = [nums.count(i) for i in nums]
    
    sCount = len(s)
    minVal = min(s)
    maxVal = max(s)
    
    
    if sCount == 1 :
        answer = 1111 * a
    elif sCount == 4 :
        answer = min(s)
        
    elif sCount == 2 :
        if min(counts) == 2 : # 주사위 2개, 2개
            answer = (maxVal + minVal) * (maxVal - minVal)
        else : # 세 주사위에서 나온 숫자가 p로 같고 나머지 다른 주사위에서 나온 숫자가 q(p ≠ q)라면 (10 × p + q)2 점을 얻습니다.
            p = nums[counts.index(3)]
            q = nums[counts.index(1)]
            
            answer = (10 * p + q) ** 2
    elif sCount == 3 : # 어느 두 주사위에서 나온 숫자가 p로 같고 나머지 두 주사위에서 나온 숫자가 각각 p와 다른 q, r(q ≠ r)이라면 q × r점을 얻습니다.
        p = nums[counts.index(2)]
        answer = (a * b * c * d) / p / p 
    
    
    
    return answer