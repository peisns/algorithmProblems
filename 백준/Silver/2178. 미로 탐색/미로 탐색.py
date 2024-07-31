n, m = [int(x) for x in input().split()]
maze = [list(input()) for _ in range(n)]
n, m, step, finish_n, finish_m = n, m, 1, n-1, m-1
queue = [[0, 0, 0]]  # queue: [[Int]]

while queue:
    x, y, step = queue.pop(0)

    if x < 0 or y < 0 or x == m or y == n or maze[y][x] == "0":
        continue
    
    step += 1
    
    if x == finish_m and y == finish_n:
        print(step)
        break
    
    maze[y][x] = "0"
    
    queue.append([x+1, y, step])
    queue.append([x-1, y, step])
    queue.append([x, y+1, step])
    queue.append([x, y-1, step])