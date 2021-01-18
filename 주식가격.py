def solution(prices):
    answer = []
    j=0
    for i in range(len(prices)):
        for j in range(i+1,len(prices),1):
            if prices[i]>prices[j]:
                break
        answer.append(j-i)
    return answer
print(solution([1, 2, 3, 2, 3]))