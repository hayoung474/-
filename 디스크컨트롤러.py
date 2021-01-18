import heapq

def solution(jobs):
    answer=0
    cnt=0
    last=-1
    heap = []
    jobs.sort()
    time = jobs[0][0]
    while cnt < len(jobs):
        for s, t in jobs:
            if last < s <= time:
                heapq.heappush(heap, (t, s))
        if heap:
            term, start = heapq.heappop(heap)
            last = time
            time += term
            answer += (time - start)
            cnt += 1
        else:
            time += 1
    return answer // len(jobs)