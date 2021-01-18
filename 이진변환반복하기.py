def solution(s):
    zero_count=0
    try_count=0
    while len(s) !=1:
        try_count+=1
        for item in s:
            if item=='0':
                zero_count+=1
        s = s.replace('0',"")
        s = str(format(len(s),'b'))
    return [try_count,zero_count]






