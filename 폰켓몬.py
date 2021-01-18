def solution(nums):
    length = len(nums)/2
    nums=list(set(nums))
    if length < len(nums):
        return length
    else:
        return len(nums) 
    
    print(nums)
solution([3,3,3,3,3,2,2,2,2])