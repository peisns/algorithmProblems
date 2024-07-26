from collections import defaultdict

alphabet_dictionary = defaultdict(int)
for alphabet in input():
    alphabet_dictionary[alphabet] += 1

def return_palindrome(dictionary) -> str:
    failure_result = "I'm Sorry Hansoo"
    half_palindrome = ""
    centerAlphabet = ""
    odd_case = 0
    
    for key, value in sorted(dictionary.items()):
        if not value % 2 == 0:
            odd_case += 1
            if odd_case > 1:
                return failure_result
            else:
                centerAlphabet = key
            
        half_palindrome += key * int(value / 2)
    
    return half_palindrome + centerAlphabet + half_palindrome[::-1]


print(return_palindrome(alphabet_dictionary))