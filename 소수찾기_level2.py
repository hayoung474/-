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

def solution(numbers):
    numbers_list = list(numbers)
    temp_list=[]
    answer_list=[]
    for i in range(1,len(numbers_list)+1):
        temp_list += list(map(''.join, itertools.permutations(numbers_list,i)))
    temp_list = list(map(int, temp_list))
    temp_list = set(temp_list) 
    temp_list = list(temp_list)
    for item in temp_list:
        if prime_check(item):
            answer_list.append(item)


    return len(answer_list)

print(solution("011"))

