def solution(number, k):


    i = 0
    j = 0
    while i < k:

        for j in range(len(number)-1):

            if(i == k):
                break

            if int(number[j]) < int(number[j+1]):
                break

        number = number[:j] + number[j+1:]
        i += 1

    return number


print(solution("1234567", 2))
