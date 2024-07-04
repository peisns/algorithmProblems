n = int(input())
int_list = list(map(int, input().split()))
min = 1000000
max = -1000000

for int in int_list:
    if int < min:
        min = int
    if int > max:
        max = int
        
print(min, max)