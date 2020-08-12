### [프로그래머스] 2018 KAKAO BLIND RECRUITMENT[1차] : 추석 트래픽 LEVEL3

------------

황금까마귀 쿠모 문제풀이 팀에서 정한 이번주 문제이다.
내 힘으로 온전히 풀지는 못했고 아래의 사이트의 도움을 받았다.
문제 이해는 완료하였지만 도움을 받았기에 많이 찝찝하다 ,,,

[사이트 바로가기 ](https://softworking.tistory.com/379)

------------

datetime 객체도 대소 비교가 가능하다. 
하지만 이 코드 같은 경우는 문자열로 변경하였는데도 오름차순 정렬이 가능했다. 
이유는 잘 모르겠지만 되는걸 확인 하였으니..

------------
##### 전체코드

```python

import datetime


def solution(lines):
    works=[]

    for line in lines:
   
        time = line.split(' ')[0]+" "+line.split(' ')[1]

        # 소수점 정렬 ( 정렬하고 보니 쓸모가 없었다 .. )
        T = float(format(float(line.split(' ')[2].replace("s", "")), ".3f"))
        
        # 문자열을 datetime 객체로 변환해 주는 과정
        time = datetime.datetime.strptime(time,"%Y-%m-%d %H:%M:%S.%f")
        # 시간 덧셈
        start = time - datetime.timedelta(seconds=T)
        # datetime 객체를 문자열로 변환해 주는 과정
        start = start.strftime("%Y-%m-%d %H:%M:%S.%f")

        # 999ms (1초) 내로 다른 작업이 시작되면 이는 동시 작업으로 본다.
        end = time + datetime.timedelta(milliseconds=999)
        end = end.strftime("%Y-%m-%d %H:%M:%S.%f")

        # 시작 시간은 "start" 라는 문자열과 함께 리스트에 담아 works 리스트에 추가한다.
        works.append([start,"start"])
        # 종료 시간도 마찬가지로 "end" 라는 문자열과 함께 리스트에 담아 works 리스트에 추가한다.
        works.append([end,"end"])
        

    # 시간을 기준으로 오름차순 정렬한다. 이를 이용하여 시간 순으로 작업의 진행 정도를 알 수 있다. 
    # ex. start start end start end end start end ... 
    
    works = sorted(works, key = lambda x : x[0])
  
    max_work = 0
    work_count=0
    
    # works 리스트를 순회한다. 만약에 start 라면 작업카운트를 +1 하고 end 라면 -1 한다.
    
    for work in works:
        if(work[1] == "start"):
            work_count += 1 
        elif (work[1] == "end"):
            work_count -= 1
        
        max_work = max(max_work,work_count)
    # 최대값을 구하여 반환한다.
    print(max_work)
    return max_work



lines = [
    "2016-09-15 01:00:04.002 2.0s",
    "2016-09-15 01:00:07.000 2s"
]

solution(lines)
```
