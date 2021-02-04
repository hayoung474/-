
N , M = map(int,input().split())
card = list(map(int,input().split()))

# num_list = list(itertools.combinations(nums,3))
# for num in num_list:
#     temp = sum(num)
#     if (temp not in sum_list) and temp <= int(M):
#         sum_list.append(temp)

total_list=[]
answer=0
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            total = card[i] + card[j] + card[k]
            if total > M :
                continue
            else:
                answer=max(answer,total)
            
print(answer)

# 정렬이 들어가면 시간이 오래걸린다
# 그 뭐냐 ,,, 조합은 사용하지 말 것. 시간이 오래걸린다
# 그냥 단순 3중포문 사용, 최댓값 max 를 사용