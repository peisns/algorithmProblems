from sys import stdin

n, m = stdin.readline().split()
numbers = [int(x) for x in stdin.readline().split()]

sum = 0
sum_array = [0]
for number in numbers:
    sum += number
    sum_array.append(sum)

def solution(i: int, j: int) -> int:
    return sum_array[j] - sum_array[i-1]

for _ in range(int(m)):
    i, j = [int(x) for x in stdin.readline().split()]
    print(solution(i, j))