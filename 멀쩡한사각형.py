def solution(w,h):
    answer = 1
    dx = w-1
    dy = h-1
    x=0.0
    y=0.0
    xinc=0
    yinc=0
    step=0

    count =0

    if abs(dx)>abs(dy):
        step = abs(dx)
    else:
        step = abs(dy)

    xinc = dx / float(step)
    yinc = dy / float(step)
    print(xinc,yinc)

    for i in range(step):
        x += xinc
        y += yinc
        count+=1



    return count

print(solution(8,12))