def solution(myString):
    answer = []
    
    answer = myString.split('x')
    answer.sort()
    answer = ' '.join(answer).split()
    return answer