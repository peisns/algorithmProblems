alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet_dictionary = {}
for character in alphabet:
    alphabet_dictionary[character] = 0

word_inputed = input()

for character in word_inputed:
    alphabet_dictionary[character] += 1
    
print(" ".join([str(x[1]) for x in sorted(alphabet_dictionary.items())]))