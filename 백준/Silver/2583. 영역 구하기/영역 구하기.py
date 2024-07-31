m, n, k = [int(x) for x in input().split()]
matrix = [[True for _ in range(n)] for _ in range(m)]
vertices = [[int(x) for x in input().split()] for _ in range(k)]

for left_x, left_y, right_x, right_y in vertices:
    for y in range(left_y, right_y):
        for x in range(left_x, right_x):
            matrix[y][x] = False

count = 0
areas = []

def get_area(y:int, x:int) -> int:
    area = 0
    queue = [(y, x)]
    
    while queue:
        i, j = queue.pop(0)
        if i < 0 or j < 0 or i == m or j == n or matrix[i][j] is False: 
            continue
        area += 1
        matrix[i][j] = False
                    
        queue.append((i+1, j))
        queue.append((i-1, j))
        queue.append((i, j+1))
        queue.append((i, j-1))
    
    return area
    
for y in range(m):
    for x in range(n):
        if matrix[y][x]:
            count += 1
            areas.append(get_area(y, x))

print(count)
print(" ".join(map(str, sorted(areas))))