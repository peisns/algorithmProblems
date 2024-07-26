from collections import defaultdict

test_case = int(input())

def get_number_of_case() -> int:
    cloth_count = int(input())
    type_count_dictionary = defaultdict(int)
    
    for _ in range(cloth_count):
        _, type = input().split()
        type_count_dictionary[type] += 1
        
    reduce_result = 1
    
    for _, n in type_count_dictionary.items():
        reduce_result *= (n + 1)
    
    reduce_result -= 1
    
    return reduce_result 

for _ in range(test_case):
    print(get_number_of_case())