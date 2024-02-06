import numpy as np

def is_col_possible(string_with_num):
    num = int(string_with_num.split()[0])
    if "red" in string_with_num:
        if num <= maxR:
            return True
        else:
            return False
    elif "green" in string_with_num:
        if num <= maxG:
            return True
        else:
            return False
    elif "blue" in string_with_num:
        if num <= maxB:
            return True
        else:
            return False
    else:
        return False
    
def is_set_impos(set_list):
    for r in set_list:
        if not is_col_possible(r):
            return True
        
    return False

f = open("input.txt", "r")
lines = f.readlines()
out=0

maxR=12
maxG=13
maxB=14

lineNum = None

for line in lines:

    line = line.rstrip()
    line = line.replace(":", ";")
    line = line.replace("Game ", "")
    game_rounds = line.split("; ")
    lineNum = int(game_rounds.pop(0))
    add_line_num = True

    for set_str in game_rounds:
        set = set_str.split(", ")
        if is_set_impos(set):
            add_line_num = False
        
    if add_line_num:
        out = out + lineNum

print(out)
