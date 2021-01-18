
def solution(dartResult):
    answer = 0
    score= 0
    i=0
    while(i != len(dartResult)):
        print(i)
        print(dartResult[i])

        if dartResult[i] == "S":
            score += int(dartResult[i-1])**1
        if dartResult[i] == "D":
            score += int(dartResult[i-1])**2
        if dartResult[i] == "T":
            score += int(dartResult[i-1])**3
        if dartResult[i] == "*":
            score *= 2
            answer += score
            score =0
        if dartResult[i] == "#":
            score *=-1
            answer += score
            score =0
        print("score:",score)
        i+=1
    return answer
        

print(solution("1S2D*3T"))