import sys

n = int(input())
input = sys.stdin.readline
list = [False] * 21

def add(n):
    list[int(n)] = True
def remove(n):
    list[int(n)] = False
def check(n):
    if list[int(n)]:
        print(1)
    else:
        print(0)
def toggle(n):
    list[int(n)] = False if list[int(n)] else True
def all(_):
    list[:] = [True] * 21
def empty(_):
    list[:] = [False] * 21
    
dict = { "add" : add, "remove" : remove, "check" : check, "toggle" : toggle, "all" : all, "empty" : empty }

for _ in range(n):
    input_list = input().rstrip().split()
    num = input_list[-1]
    dict[input_list[0]](num)