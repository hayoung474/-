def solution(priorities, location):
    answer = 0
    temp_list = [[num,False] for num in priorities]
    temp_list[location][1]=True
    count=0

    while(len(temp_list)!=0):
        
        if len(temp_list) == 1:
            count+=1
            if temp_list[0][1]==True:
                answer=count
            temp_list.pop(0)
            break
        if temp_list[0][0] < max(map(max, temp_list[1:])):
            temp_list.append(temp_list[0])
            temp_list.pop(0)
            
        else:
            count+=1
            if temp_list[0][1]==True:
                answer=count
            temp_list.pop(0)
    return answer
solution([2, 1, 3, 2],2)