def solution(n):
    temp_list = list(map(int,str(n)))
    temp_list = sorted(temp_list, reverse = True)
    temp_list = list(map(str, temp_list))
    return int("".join(temp_list))

print(solution(118372))