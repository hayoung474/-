import heapq

def solution(operations):
    heap=[]
    for oper in operations:
        if oper[0] == 'I':
            heapq.heappush(heap,int(oper[1:]))
        elif heap:
            if oper == 'D -1':
                heapq.heappop(heap)
            elif oper =="D 1":
                heap.remove(max(heap))

    if heap:
        return [max(heap),heap[0]]
    else:
        return [0,0]