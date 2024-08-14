def is_possible(string) -> bool:
    list = ""
    for char in string:
        list += char
        len_list = len(list)
        if len_list == 1:
            continue
        elif len_list == 2 and (list == "pi" or list == "ka"):
            list = ""
        elif len_list == 3:
            if list == "chu":
                list = ""
            else:
                return False
    if list != "":
        return False
    return True

print("YES" if is_possible(input()) else "NO")