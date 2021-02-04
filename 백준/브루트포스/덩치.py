
N = int(input())
person_list=[]
answer = [1]*N
for _ in range(N):
    person_list.append(list(map(int,input().split())))
    
for j in range(N):
    for k in range(N):
        if person_list[j][0] > person_list[k][0] and person_list[j][1] > person_list[k][1]:
            answer[k]+=1
for l in range(N):
    print(answer[l], end=' ')
