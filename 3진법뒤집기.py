def solution(n):
    num = str(dec2ter(n))
    num = int(''.join(reversed(num)))
    return int(str(num),3)

def dec2ter(n):
    number=""
    remainder = 0
    while(n>0):
        remainder = n % 3 
        if(n%3 == 0):
            n = (n//3)
        else:
            n = n//3
        number = str(remainder)+number
    return number
