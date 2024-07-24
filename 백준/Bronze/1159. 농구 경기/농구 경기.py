from collections import Counter

N = int(input())
character_list = [input()[0] for _ in range(N)]

counter = Counter(character_list)
filtered_list = list(filter(lambda x: x[1] >= 5, counter.items()))

result = sorted(map(lambda x: x[0], filtered_list))
print("".join(result) if len(result) != 0 else "PREDAJA")