def solution(numbers):
    answer = []
    num=0
    for i in range(len(numbers)-1):
        for j in range(i+1,len(numbers),1):
            num = numbers[i] + numbers[j]
            if(num not in answer):
                answer.append(num)
    answer.sort()
    return answer



numbers = [2,1,3,4,1]

print(solution(numbers))