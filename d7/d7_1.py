def process_input():
    f = open("input.txt", "r")
    lines = f.readlines()
    input=[]
    for line in lines:
        line = line.rstrip().split()
        line[1] = int(line[1])
        input.append(line)
    return input

def get_val(c):
    if c.isnumeric:
        return int(c)
    elif c == 'T':
        return 10
    elif c == 'J':
        return 11
    elif c == 'Q':
        return 12
    elif c == 'K':
        return 13
    elif c == 'A':
        return 14

def hand_strength(hand):
    arr = list(hand)
    arr.count(arr)
    

out=0
input = process_input()

