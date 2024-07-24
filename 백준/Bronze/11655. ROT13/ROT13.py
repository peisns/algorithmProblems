number_ord_z = ord("z")
number_ord_Z = ord("Z")


def rot13(word: str) -> str:
    if word in " 0123456789":
        return word
    
    number = ord(word) + 13
    
    if word.islower():
        return chr(number) if number <= number_ord_z else chr(number - 26)
    else:
        return chr(number) if number <= number_ord_Z else chr(number - 26)


print("".join(map(rot13, input())))