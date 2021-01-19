import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    L = len(scoville) # scoville 힙의 크기를 저장해두어야 함.
    f = heapq.heappop(scoville) # 순서 중요!!!!!!!!
    for i in range(1,L):
        s= heapq.heappop(scoville)
        f = heapq.heappushpop(scoville,f+s*2)
        if f>=K: return i
    return -1


print(solution([1,2,3],11))
# def solution(scoville, K):
#     heapq.heapify(scoville)
#     count=0
#     while scoville[0]<=K:
#         f= heapq.heappop(scoville)
#         s= heapq.heappop(scoville)
#         heapq.heappush(scoville,f+(s*2))
#         count+=1   

    
    #return count
# def solution(scoville, K):
#     heapq.heapify(scoville)
#     count=0
#     while scoville[0]<=K:
#         f= heapq.heappop(scoville)
#         if len(scoville)==0: # 이 조건 추가로 성공할 수 있었음. 시간은 좀 더 걸림.
#             return -1
#         s= heapq.heappop(scoville)
#         heapq.heappush(scoville,f+(s*2))
#         count+=1   
#     return count

# 효율이 나오지 않는 코드 ... 
# pushpop 을 활용하여 속도를 높임.
# 조건검사를 줄임.
# 안되는 이유는 스코빌 지수를 K이상 높잎 수 없을때 -1 반환하는 조건을 만들지 않음.
# while 문을 사용하면 탈출이 어려울 수 있으니 for 문을 사용

