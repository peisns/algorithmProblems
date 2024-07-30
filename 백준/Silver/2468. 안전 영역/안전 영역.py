import copy

n = int(input())
land_list = [[int(x) for x in input().split()] for _ in range(n)]
max_height = max(map(max, land_list))

unsubmerged_land_coordinate_list = []
for i in range(n):
    for j in range(n):
        unsubmerged_land_coordinate_list.append([i, j])

unsubmerged_land_count = 0

def get_unsubmerged_land_count(temp_land_list) -> int:
    count = 0
    
    for y, x in unsubmerged_land_coordinate_list:
        if temp_land_list[y][x]:
            count += 1
            
            queue = [(y, x)]
            while queue:
                y, x = queue.pop(0)
                if y < 0 or x < 0 or y == n or x == n or temp_land_list[y][x] is False:
                    continue
                
                temp_land_list[y][x] = False
                queue.append((y+1, x))
                queue.append((y-1, x))
                queue.append((y, x+1))
                queue.append((y, x-1))
    
    return count

for water_level in range(0, max_height):
    
    for i in range(len(unsubmerged_land_coordinate_list)-1, -1, -1):
        y, x = unsubmerged_land_coordinate_list[i]
        land_level = land_list[y][x]
        
        if land_level <= water_level:
            unsubmerged_land_coordinate_list.pop(i)
            land_list[y][x] = False
    
    temp_land_list = copy.deepcopy(land_list)
    unsubmerged_land_count = max(
        get_unsubmerged_land_count(temp_land_list),
        unsubmerged_land_count)
        
print(unsubmerged_land_count)