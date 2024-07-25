import sys

N, M = [int(x) for x in input().split()]
number_pokemon_dictionary = {}
pokemon_number_dictionary = {}

for i in range(1, N + 1):
    pokemon = sys.stdin.readline()[:-1]
    number_pokemon_dictionary[i] = pokemon
    pokemon_number_dictionary[pokemon] = i


def return_result(text) -> str:
    if text[0].isdigit():
        return number_pokemon_dictionary[int(text[:-1])]
    else:
        return str(pokemon_number_dictionary[text[:-1]])


for _ in range(M):
    print(return_result(sys.stdin.readline()))