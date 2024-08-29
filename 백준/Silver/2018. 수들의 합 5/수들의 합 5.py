n = int(input())
i = 0
j = 0
temp = 0
count = 0
last_i = n-1

while i < last_i:
    if temp > n:
        i += 1
        temp -= i
        continue

    if temp == n:
        count += 1
    
    j += 1
    if j == n:
        break
    temp += j
    
print(count+1)