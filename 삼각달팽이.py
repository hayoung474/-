def solution(n):
    answer = []
    triangle_snail = []
    for i in range(1,n+1):
        triangle_snail.append([0]*i)
    max_count=n *(n+1)//2 # 네모 칸 개수 구하기
    count=0
    for j in range(1):
        for i in range(0,len(triangle_snail)):
            count+=1
            triangle_snail[i][0]=count
        for k in range(1,len(triangle_snail[-1])):
            count+=1
            triangle_snail[-1][k]=count
        for l in range(len(triangle_snail)-2,0,-1):
            count+=1
            triangle_snail[l][-1]=count

        count+=1
        triangle_snail[2][1]=count

        count+=1
        triangle_snail[3][1]=count
    print(triangle_snail)
solution(5)