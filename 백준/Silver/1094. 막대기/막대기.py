n = int(input())
sum = 64
list = [64]
while not n == sum:
    last_element = list.pop(-1)
    half = last_element / 2
    sum -= half
    list.append(half)
    
    if sum < n:
        list.append(half)
        sum += half

print(len(list))