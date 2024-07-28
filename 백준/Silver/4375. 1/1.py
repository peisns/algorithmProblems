def find_number() -> int:
    n = int(input())
    
    string_number = "1"
    
    while not int(string_number) % n == 0:
        string_number += "1"
    
    return len(string_number)
   
try:
    while True:
        print(find_number())
except:
    pass