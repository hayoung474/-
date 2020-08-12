import datetime


def solution(lines):
    works=[]

    for line in lines:
   
        time = line.split(' ')[0]+" "+line.split(' ')[1]

        # 소수점 정렬
        T = float(format(float(line.split(' ')[2].replace("s", "")), ".3f"))
        
        time = datetime.datetime.strptime(time,"%Y-%m-%d %H:%M:%S.%f")
        start = time - datetime.timedelta(seconds=T)
        start = start.strftime("%Y-%m-%d %H:%M:%S.%f")

        # 999ms 내로 다른 작업이 시작되면 이는 동시 작업 
        end = time + datetime.timedelta(milliseconds=999)
        end = end.strftime("%Y-%m-%d %H:%M:%S.%f")

        works.append([start,"start"])
        works.append([end,"end"])

    # 시간을 기준으로 오름차순 정렬
    works = sorted(works, key = lambda x : x[0])

    max_work = 0
    work_count=0
    
    for work in works:
        if(work[1] == "start"):
            work_count += 1 
        elif (work[1] == "end"):
            work_count -= 1
        
        max_work = max(max_work,work_count)
        
    print(max_work)
    return max_work



lines = [
    "2016-09-15 01:00:04.002 2.0s",
    "2016-09-15 01:00:07.000 2s"
]

solution(lines)
