import numpy as np

def check_min_color(string_with_num, minR, minG, minB):
    num = int(string_with_num.split()[0])
    if "red" in string_with_num:
        if minR is None:
            minR = num
        else:
            minR = min(minR, num)
    elif "green" in string_with_num:
        if minG is None:
            minG = num
        else:
            minG = min(minG, num)
    elif "blue" in string_with_num:
        if minB is None:
            minB = num
        else:
            minB = min(minB, num)
    return
    
def min_in_set(set, minR, minG, minB):
    for s in set:
        num = int(s.split()[0])
        if "red" in s:
            if minR is None:
                minR = num
            else:
                minR = min(minR, num)
        elif "green" in s:
            if minG is None:
                minG = num
            else:
                minG = min(minG, num)
        elif "blue" in s:
            if minB is None:
                minB = num
            else:
                minB = min(minB, num)

def set_default(minC):
    if minC is None:
        return 0
    else:
        return minC

f = open("input.txt", "r")
lines = f.readlines()
out=0

minR=None
minG=None
minB=None

lineNum = None

for line in lines:
    minR=None
    minG=None
    minB=None

    line = line.rstrip()
    line = line.replace(":", ";")
    line = line.replace("Game ", "")
    game_rounds = line.split("; ")
    lineNum = int(game_rounds.pop(0))
    add_line_num = True

    for set_str in game_rounds:
        set = set_str.split(", ")
        for s in set:
            num = int(s.split()[0])
            if "red" in s:
                if minR is None:
                    minR = num
                else:
                    minR = max(minR, num)
            elif "green" in s:
                if minG is None:
                    minG = num
                else:
                    minG = max(minG, num)
            elif "blue" in s:
                if minB is None:
                    minB = num
                else:
                    minB = max(minB, num)
        
    minR = set_default(minR)
    minG = set_default(minG)
    minB = set_default(minB)

    out += minR*minG*minB

print(out)
