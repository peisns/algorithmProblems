def solution(numbers, hand):
    number_dictionary = {1: "L", 3: "R", 4: "L", 6:"R", 7: "L", 9:"R"}
    xy_dictionary = {1:[0, 0], 2:[0, 1], 3:[0, 2], 
                     4:[1, 0], 5:[1, 1], 6:[1, 2],
                     7:[2, 0], 8:[2, 1], 9:[2, 2],
                     "*":[3, 0], 0: [3, 1], "#":[3, 2]
                    }
    left = "*"
    right = "#"
    
    answer = ''
    
    for number in numbers:
        if number in number_dictionary:
            finger = number_dictionary[number]
            answer += finger
            if finger == "L":
                left = number
            else:
                right = number
        else:
            left_y, left_x = xy_dictionary[left]
            right_y, right_x = xy_dictionary[right]
            number_y, number_x = xy_dictionary[number]
            left_distance = abs(number_y - left_y) + abs(number_x - left_x)
            right_distance = abs(number_y - right_y) + abs(number_x - right_x)
            
            if left_distance < right_distance:
                answer += "L"
                left = number
            elif right_distance < left_distance:
                answer += "R"
                right = number
            elif hand == "left":
                answer += "L"
                left = number
            else:
                answer += "R"
                right = number
            
    return answer