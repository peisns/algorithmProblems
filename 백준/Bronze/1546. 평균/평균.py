n = int(input())
scores = [int(x) for x in input().split()]
max_score = max(scores)
sum = sum(scores)
print(sum / max_score * 100 / n)