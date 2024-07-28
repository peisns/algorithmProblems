A, B, C = [int(x) for x in input().split()]

remainder = A % C
more_multiple = []

while B != 1:
    if B % 2 != 0:
        more_multiple.append(remainder)
    remainder = remainder * remainder % C
    B = B // 2

while more_multiple:
    remainder = remainder * more_multiple.pop(-1) % C

print(remainder)