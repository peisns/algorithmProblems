N, K = [int(x) for x in input().split()]  #

temperatures = [int(x) for x in input().split()]

sum_temperature = sum(temperatures[:K])
max_temperature = sum_temperature

for i in range(K,N):
    sum_temperature += temperatures[i]
    sum_temperature -= temperatures[i-K]
    if sum_temperature > max_temperature:
        max_temperature = sum_temperature

print(max_temperature)