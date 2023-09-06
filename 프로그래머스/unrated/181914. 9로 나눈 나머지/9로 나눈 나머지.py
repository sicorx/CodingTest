def solution(number):
    answer = 0
    tmp = 0
    for i in range(len(number)) :
        tmp += int(number[i])
    answer = tmp % 9
    return answer