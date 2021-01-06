def solution(n):
    answer = ''
    remainder = 0
    while(n>0):
        remainder = n % 3 
        if(n%3 == 0):
            n = (n//3) -1
            remainder = 4
        else:
            n = n//3
        answer = str(remainder)+answer
    return answer

print(solution(10))

