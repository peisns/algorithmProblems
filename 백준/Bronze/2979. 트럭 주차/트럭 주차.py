a, b, c = [int(x) for x in input().split()]
in_time_dictionary, out_time_dictionary = {}, {}
car_count, result = 0, 0

for _ in range(3):
    in_time, out_time = [int(x) for x in input().split()]
    
    in_time_dictionary[in_time] = 1 if in_time not in in_time_dictionary else in_time_dictionary[in_time] + 1
    out_time_dictionary[out_time] = 1 if out_time not in out_time_dictionary else out_time_dictionary[out_time] + 1

for time in range(101):
    
    if time in in_time_dictionary:
        car_count += in_time_dictionary[time]
    
    if time in out_time_dictionary:
        car_count -= out_time_dictionary[time]
    
    if car_count == 1:
        result += a
    elif car_count == 2:
        result += b * 2
    elif car_count == 3:
        result += c * 3

print(result)