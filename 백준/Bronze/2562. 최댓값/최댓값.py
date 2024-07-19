result = 0
index = 0

for i in range(9):
    num = int(input())
    if num >= result:
        result = num
        index = i

print(result)
print(index + 1)