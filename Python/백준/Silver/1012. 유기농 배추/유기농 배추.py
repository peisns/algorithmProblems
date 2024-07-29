def spread_worm(x: int, y: int, farm: [[bool]], m: int, n: int, queue: [[int]]):
    if x < 0 or y < 0 or x == m or y == n or farm[y][x] is False:
        return 
    farm[y][x] = False
    
    queue.append([x-1, y])
    queue.append([x+1, y])
    queue.append([x, y-1])
    queue.append([x, y+1])


def get_worm_count() -> int:
    m, n, k = [int(x) for x in input().split()]
    farm = [[False for _ in range(m)] for _ in range(n)]
    worm_count = 0
    
    for _ in range(k):
        x, y = [int(x) for x in input().split()]
        farm[y][x] = True
        
    for y in range(n):
        for x in range(m):
            if farm[y][x] is False:
                continue
            
            worm_count += 1
            queue = [(x, y)]
            while queue:
                i, j = queue.pop(0)
                spread_worm(i, j, farm, m, n, queue)
    
    return worm_count
    
for _ in range(int(input())):
    print(get_worm_count())