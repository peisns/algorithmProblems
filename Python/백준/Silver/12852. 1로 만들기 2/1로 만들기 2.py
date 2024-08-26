n = int(input())

stack = [(0, [n])] if n != 1 else []
result_count = 1000000 if n != 1 else 0
result_list = [] if n != 1 else [1]

def isOne(count, temp_list) -> bool:
    if temp_list[-1] == 1:
        global result_count
        result_count = count
        global result_list
        result_list = temp_list
        return True
    else:
        stack.append((count, temp_list))
        return False
        

while stack:
    count, order_list = stack.pop(-1)
    
    count += 1
    
    if count >= result_count:
        continue
    
    temp_list = order_list[:]
    temp_list.append(temp_list[-1]-1)
    if isOne(count, temp_list):
        continue
            
    temp_list = order_list[:]
    if temp_list[-1] % 2 == 0:
        temp_list.append(temp_list[-1]/2)
        if isOne(count, temp_list):
            continue
            
    temp_list = order_list[:]
    if temp_list[-1] % 3 == 0:
        temp_list.append(temp_list[-1]/3)
        if isOne(count, temp_list):
            continue
    

print(result_count)
print(" ".join([str(int(x)) for x in result_list]))