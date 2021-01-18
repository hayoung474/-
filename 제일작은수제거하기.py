def solution(arr):
    arr.pop(arr.index(min(arr)))
    if len(arr) ==0:
        return [-1]
    return arr
print(solution([1,5,3,2,4,3]))