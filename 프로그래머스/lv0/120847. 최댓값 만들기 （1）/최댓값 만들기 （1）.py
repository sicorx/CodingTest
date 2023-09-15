def solution(numbers):
    answer = max(numbers)
    numbers.remove(max(numbers))
    answer *= max(numbers)
    
    return answer