def solution(s):
    return (len(s)==4 or len(s)==6)and(s.isdigit())

# isdigit 은 문자열이 숫자인지 아닌지 검사하는 함수

print(solution('1244'))