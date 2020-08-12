
numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = "left"

def calcDistance(number,currentHand):
    keypad=[[1,2,3],[4,5,6],[7,8,9],[10,0,11]]

    for idx in keypad:
        if number in idx:
            x1= keypad.index(idx)
            y1= idx.index(number)
    for idx in keypad:
        if currentHand in idx:
            x2 = keypad.index(idx)
            y2 =idx.index(currentHand)

    return (abs(x1-x2)+abs(y1-y2))


def solution(number,hand):
    answer=""
    currentRightHand = 11
    currentLeftHand = 10
    RightStep = 0
    LeftStep = 0


    for n in numbers:
        if n in [1,4,7]:
            answer+="L"
            currentLeftHand = n

        elif n in [3,6,9]:
            answer+="R"
            currentRightHand = n
        else:
            RightStep = calcDistance(n,currentRightHand)
            LeftStep = calcDistance(n,currentLeftHand)

            if (RightStep > LeftStep):
                answer+="L"
                currentLeftHand = n
            elif (RightStep < LeftStep):
                answer+="R"
                currentRightHand = n
            elif(RightStep == LeftStep):
                if(hand == "right"):
                    answer+="R"
                    currentRightHand = n
                elif (hand == "left"):
                    answer+="L"
                    currentLeftHand = n
        print(currentRightHand,currentLeftHand)
    return answer

print(solution(numbers,hand))