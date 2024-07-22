from collections import namedtuple
import copy

height_list = sorted([int(input()) for _ in range(9)])

nt = namedtuple('nt', ['height_list', 'total_height'])

queue = [nt(height_list, sum(height_list))]

result = []

isEnd = False

while not isEnd:
    element = queue.pop(0)
    len_list = len(element.height_list)
    
    for i in range(len_list):
        temp_list = copy.deepcopy(element.height_list)
        num = temp_list[i]
        total_height = element.total_height - num
        temp_list.pop(i)
        if len_list != 8:
            queue.append(nt(temp_list, total_height))
        elif len_list == 8 and total_height == 100:
            isEnd = True
            result = temp_list
                
for num in result:
    print(num)