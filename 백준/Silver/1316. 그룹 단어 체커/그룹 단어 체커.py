n = int(input())
word_list = [input() for _ in range(n)]


def is_group_word(word: str) -> bool:
    character_set = set([word[0]])

    for i in range(1, len(word)):
        char = word[i]
        if character_set.issuperset(char) and word[i - 1] != char:
            return False
        character_set.add(char)
    return True


result = len(list(filter(is_group_word, word_list)))

print(result)