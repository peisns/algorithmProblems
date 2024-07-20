NM = [int(x) for x in input().split()]
N, M = NM[0], NM[1]

ijk_list = [[int(x) for x in input().split()] for _ in range(M)]

basket_list = [0 for _ in range(N)]

for list in ijk_list:
    i, j, k = list[0] - 1, list[1], list[2]
    basket_list[i:j] = [k for _ in range(j - i)]

print((" ").join([str(x) for x in basket_list]))