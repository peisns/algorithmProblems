import math
import copy

n = int(input())
total_step = int(math.log2(n))
points = [list(input()) for _ in range(n)]
bools_list = [[[True] * n for _ in range(n)]]


def is_same(i:int, j:int , step:int, last_bools: [[int]], bools:[[int]]):
    point = points[i][j]
    for y in range(i, i+int(pow(2, step+1)), int(pow(2, step))):
        for x in range(j, j+int(pow(2, step+1)), int(pow(2, step))):
            if not points[y][x] == point or not last_bools[y][x]:
                bools[i][j] = False
                return 
    return 


for step in range(total_step):
    last_bools = bools_list[-1]
    bools = [[True] * n for _ in range(n)]
    for i in range(0, n, int(pow(2, step+1))):
        for j in range(0, n, int(pow(2, step+1))):
            is_same(i, j, step, last_bools, bools)
    bools_list.append(bools)
    

def get_str(i: int, j:int, step: int) -> str:
    if step == 0 or bools_list[step][i][j]:
        return f"{points[i][j]}"
    sub_points = []
    for y in range(i, i+int(pow(2, step)), int(pow(2, step-1))):
        for x in range(j, j+int(pow(2, step)), int(pow(2, step-1))):
            sub_points.append(get_str(y, x, step-1))
            
    return f'({"".join(sub_points)})'


print(get_str(0, 0, total_step))