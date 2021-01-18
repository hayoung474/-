def solution(s):
    answer = s
    for i in range(len(s)):
        if s[0].islower():
            s[i].upper()
        if s[i-1]==" ":
            s[i].upper()
    return answer
print(solution("3people unFollowed me"))