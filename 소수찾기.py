def solution(n):
    answer=0
    for i in range(1,n+1):
        print(i,":",Prime(i))
        if(Prime(i)):
            answer+=1
    return answer


def Prime(n):
    if(n<2):
        return False
    else:
        for i in range(2,n):
            if(n%i == 0):
                return False
        
    return True

solution(10)