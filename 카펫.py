def solution(brown, yellow):

    divisor_list=[]
    if yellow == 1:
        return [3,3]
    for i in range(1,yellow+1,1):
        if yellow % i == 0:
            divisor_list.append(i)
    while(True):
        if len(divisor_list) != 0 :
            width = divisor_list[-1]
            height = divisor_list[0]
        else:
            width = divisor_list[0]
            height = divisor_list[0]

        temp_brown = (width*2)+(height*2)+4
        if temp_brown == brown:
            return [width+2,height+2]
        else:
            divisor_list.pop()
            divisor_list.pop(0)
        
print(solution(24,25))