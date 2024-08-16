from collections import deque
from functools import reduce

def start_ac_test():
    p = input()
    _ = input()
    array = input()[1:-1]
    dequeue = deque(array.split(",")) if len(array) > 0 else deque([])
    is_direction_left = True
    for char in p:
        if char == "R":
            is_direction_left = not is_direction_left
        else:
            if len(dequeue) == 0:
                print("error")
                return
            if is_direction_left:
                dequeue.popleft()
            else:
                dequeue.pop()
    
    if dequeue:
        list_of_dequeue = list(dequeue) if is_direction_left else list(dequeue)[::-1]
        result = reduce(lambda x, y: f"{x},{y}", list_of_dequeue)
        print("[" + result + "]")
    else:
        print("[]")
    
for _ in range(int(input())):
    start_ac_test()