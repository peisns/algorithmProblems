r, c = [int(x) for x in input().split()]
maze = [list(input()) for _ in range(r)]

set_J = set()
set_F = set()

for i in range(r):
    for j in range(c):
        char = maze[i][j]
        match char:
            case "J":
                set_J.add((i, j))
            case "F":
                set_F.add((i, j))

count = 0

is_escaped = False
    
while not is_escaped:
    
    if not set_J:
        print("IMPOSSIBLE")
        break
    
    temp_set = set(set_J)
    set_J = set()
    
    count += 1
    
    for i, j in temp_set:
        if is_escaped:
            break
        for i, j in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
            if i < 0 or i >= r or j < 0 or j >= c:
                print(count)
                is_escaped = True
                break
            
            if maze[i][j] == ".":
                maze[i][j] = "J"
                set_J.add((i, j))
        
    temp_set = set(set_F)
    set_F = set()
    
    for i, j in temp_set:
        for i, j in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
            if i < 0 or i >= r or j < 0 or j >= c:
                continue
            
            char = maze[i][j]
            if char == "." or char == "J":
                maze[i][j] = "F"
                set_F.add((i, j))
                set_J.discard((i, j))