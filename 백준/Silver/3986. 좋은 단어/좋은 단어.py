N = int(input())

good_word_count = 0

for i in range(N):
    word = input()
    
    if len(word) % 2 != 0: 
        continue
    
    stack = []
    
    for character in word:
        if len(stack) == 0:
            stack.append(character)
            continue
        
        if stack[-1] == character:
            stack.pop(-1)
            continue
        
        stack.append(character)
    
    good_word_count += 1 if len(stack) == 0 else 0
    
print(good_word_count)
