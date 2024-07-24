word = input()

def solution(word) -> int:
    n = len(word)
    half_n = n // 2
    
    for i in range(half_n):
        if word[i] != word[-(i+1)]:
            return 0

    return 1
    
print(solution(word))
