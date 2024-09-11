from collections import defaultdict

def solution(n: int, m: int, numbers: [int]) -> int:
    sums = []
    sum = 0
    for number in numbers:
        sum += number
        sums.append(sum)
    remainders = [x % m for x in sums]
    dict = defaultdict(int)
    for num in remainders:
        dict[num] += 1
    
    result = 0
    result += dict[0]
    
    for num in range(0, n):
        count = dict[num]
        if count > 1:
            result += (count * (count-1)) / 2
    
    return int(result)
    
n, m = [int(x) for x in input().split()]
numbers = [int(x) for x in input().split()]
print(solution(n, m, numbers))