import copy

r, c, k = map(int, input().split())
strings = [list(input()) for _ in range(r)]

home_j = c-1
stack = [(r-1, 0, strings, 1)]
result = 0

while stack:
    i, j, strings, count = stack.pop(-1)
    if i == 0 and j == home_j:
        if count == k:
            result += 1
        continue
    
    if i < 0 or j < 0 or i == r or j == c or count > k or strings[i][j]== "X" or strings[i][j] == "T":
        continue
    
    new_strings = copy.deepcopy(strings)
    new_strings[i][j] = "X"
    
    stack.append((i+1, j, new_strings, count+1))
    stack.append((i-1, j, new_strings, count+1))
    stack.append((i, j+1, new_strings, count+1))
    stack.append((i, j-1, new_strings, count+1))
    
print(result)