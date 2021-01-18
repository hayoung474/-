import itertools
import math

def prime_check(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0 :
        return False

    for i in range(3,int(math.sqrt(n))+1,2):
        if n % i ==0:
            return False
    return True

def solution(nums):
    comb_list = list(itertools.combinations(nums,3))
    answer=0
    for num in comb_list:
        temp = sum([int(i) for i in num])
        if prime_check(temp):
            answer+=1
            print(temp)
    return answer 

print(solution([1,6,4]))