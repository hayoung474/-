def solution(clothes):
    answer = 1
    comb={}
    for cloth in clothes:
        if cloth[1] in comb:
            comb[cloth[1]]+=1
        else:
            comb[cloth[1]]=1
    for value in comb.values():
        answer *= (value+1) #투명한 옷을 추가해서 안입는 경우를 생각하면 됨... 대박박
    return answer-1 # 모두 안입음(투명옷) 이 선택된 경우
solution([['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']])