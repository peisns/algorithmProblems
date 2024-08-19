n = int(input())
times = sorted([[int(x) for x in input().split()] for _ in range(n)])

time = 0
for x in times:
    arrival, checking = x
    if arrival > time:
        time = arrival
    time += checking

print(time)