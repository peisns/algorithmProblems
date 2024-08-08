def solution(dartResult):
    scores = []
    temp = []
    
    for char in dartResult:
        if char.isdigit():
            if char == "0" and temp:
                temp = [10]
            else:
                temp.append(int(char))
            continue
        
        if char == "S":
            scores.append(temp[0])
            temp = []
        elif char == "D":
            scores.append(int(pow(temp[0], 2)))
        elif char == "T":
            scores.append(int(pow(temp[0], 3)))
        elif char == "*":
            if len(scores) > 1:
                scores[-2] *= 2
            scores[-1] *= 2
        elif char == "#":
            scores[-1] *= -1
                
        temp = []
                
    answer = 0
    for score in scores:
        answer += score
    return answer


"""
점수 s = n
점수 d = n * n
점수 t = n * n * n

* 이전 점수, 이번 점수 2배
*의 효과는 중첩 될 수 있다

# 이전 점수 마이너스
*와 #의 효과는 중첩될 수 있다


"""