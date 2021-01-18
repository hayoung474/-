def solution(genres, plays):
    total_play={}
    best_album=[]
    for i in range(len(genres)):
        if genres[i] in total_play:
            total_play[genres[i]]+=plays[i]
        else:
            total_play[genres[i]]=plays[i]
    total_play = dict(sorted(total_play.items(), key=lambda x : x[1],reverse=True))
    
    for key in total_play.keys():
        temp=[]
        for j in range(len(genres)):
            if key == genres[j]:
                temp.append([plays[j],j])
        temp = sorted(temp, key = lambda x : (x[0], -x[1]) ,reverse=True)
        for k in range(len(temp)):
            if(k>1):
                break
            best_album.append(temp[k][1])
    return best_album


print(solution(['classic','classic','classic','classic','pop'],[500,150,800,800,2500]))