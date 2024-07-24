N = int(input())
front_word, end_word = input().split("*")
word_count = len(front_word + end_word)

def isSame(word) -> bool:
    if len(word) < word_count:
        return False
    
    for i in range(len(front_word)):
        if word[i] != front_word[i]:
            return False
    for i in range(len(end_word)):
        if word[-(i+1)] != end_word[-(i+1)]:
            return False
    return True

for _ in range(N):
    print("DA" if isSame(input()) else "NE")