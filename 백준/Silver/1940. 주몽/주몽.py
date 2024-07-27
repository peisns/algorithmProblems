from collections import defaultdict

_ = input();
m = int(input())
number_list = [int(x) for x in input().split()]

number_dictionary = defaultdict(int)

armor_count = 0

for number in number_list:
    number_dictionary[number] += 1
    
if m % 2 == 0:
    armor_count += number_dictionary[m / 2] // 2
    number_dictionary[m / 2] = 0

for number, count in dict(number_dictionary).items():
    another_number = m - number
    armor_count += min(count, number_dictionary[another_number])
    number_dictionary[number] = 0

print(armor_count)