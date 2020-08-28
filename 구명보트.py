def solution(people, limit):

    boat = 0
    i = 0

    # 오름차순으로 정렬. 
    people.sort()

    i = 0
    j = len(people)-1
    while(i < j):
        if people[i] + people[j] <= limit:
            i+=1
            j-=1
        else :
            j-=1

        boat+=1
    
    if i== j:
        boat+=1

    return boat


people = [70, 80, 50,50,20]
print(solution(people, 100))
