import heapq

def solution(jobs):
    answer=0
    cnt=0 # 수행한 작업 개수 저장을 위한 변수
    last=-1 # 마지막 작업 시간을 저장하기 위한 변수
    heap = [] #heapq 사용
    jobs.sort() # jobs 를 요청 시간을 기준으로 정렬함.
    time = jobs[0][0] # 초기 시간 설정
    while cnt < len(jobs): # 작업 갯수 (count) 만큼 while문 반복
        for s, t in jobs: # jobs 순회
            if last < s <= time: # 작업이 수행되는 도중에 작업 요청이 들어온 경우를 모두 힙으로 
                heapq.heappush(heap, (t, s)) # 최소 힙 저장을 위해 term 과 start 를 뒤집어서 저장
        if heap: # 힙 안의 작업을 term 이 짧은 순으로 pop
            term, start = heapq.heappop(heap) # 작업 pop
            last = time # 마지막 작업 시간을 저장
            time += term # 현재 시간을 term 만큼 증가 
            answer += (time - start) # 현재 시간 - 요청 시간 한 반환시간 을 answer 에 저장
            cnt += 1
        else:
            time += 1 # 힙 안에 작업이 없으면 현재시간을 ++
    return answer // len(jobs) # 반환 시간의 평균 값을 내어 정수 형태로 반환