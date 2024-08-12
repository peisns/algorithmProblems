n = int(input())
result = 1
if n < 0:
    result = 32
while not (n == 1 or n == 0 or n < 0):
    n //= 2
    result += 1

print(result)