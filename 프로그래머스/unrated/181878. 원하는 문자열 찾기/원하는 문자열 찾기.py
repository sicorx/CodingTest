def solution(myString, pat):
    answer = 0
    myString = myString.lower()
    pat = pat.lower()
    
    if myString.find(pat) >= 0 :
        answer = 1
    return answer