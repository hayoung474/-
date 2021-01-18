memo = {0:0 , 1:1} #base case 

def solution(n):
    for i in range(2,n+1):
        memo[i]=(memo[i-1]+memo[i-2])%1234567
    return memo[n]

solution(3)