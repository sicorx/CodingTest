def solution(n, words):
    answer = []

    for i in range(len(words)) :
        if len(words[i]) <= 1 :
            answer.append(i % n + 1)
            answer.append(i // n + 1)
            return answer
            
        if i != words.index(words[i]) :
            #print(i,':',words[i],':',words.index(words[i]))
            answer.append(i % n + 1)
            answer.append(i // n + 1)
            return answer
    
    for i in range(len(words) - 1) :            
        if words[i][::-1][0] != words[i+1][0] :
            #print(i+1,':', words[i+1])
            answer.append((i+1) % n + 1)
            answer.append((i+1) // n + 1)
            return answer
        
    answer.append(0)
    answer.append(0)
    return answer