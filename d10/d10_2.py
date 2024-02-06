def process_input() -> list:
    f = open("input", "r")
    lines = f.readlines()
    input=[]
    for line in lines:
        temp = list(line.rstrip())
        input.append(temp)
    return input

def find_start(input: list) -> (int, int):
    i=0
    for line in input:
        if 'S' in line:
            j = line.index('S')
            return i, j
        i+=1
    return

def flip_dir(dir: int):
    if dir == 0:
        return 2
    if dir == 1:
        return 3
    if dir == 2:
        return 0
    if dir == 3:
        return 1
    
def traverse(i: int, j: int, dir, sym) -> (int, int, int):
    # return new i, new j, new dir(c) (unflipped)
    connect_list = list(sym_dict.get(sym))
    connect_list[dir] = 0
    c=0
    for joint in connect_list:
        if joint == 1:
            if c==0:
                return (i-1, j, c)
            elif c==1:
                return (i, j+1, c)
            elif c==2:
                return (i+1, j, c)
            elif c==3:
                return (i, j-1, c)
        c+=1

sym_dict={'|': [1,0,1,0], '-': [0,1,0,1], 'L': [1,1,0,0], 'J': [1,0,0,1], '7': [0,0,1,1], 'F': [0,1,1,0], '.': [], 'S': [1,0,0,1]}
input = process_input()
area_input=input.copy()
loop_indices=[]
i, j = find_start(input)
loop_indices.append((i,j))

# i - line, j - index in line
dir=3
cur_sym = input[i][j]
i, j, dir = traverse(i, j, dir, cur_sym)
loop_indices.append((i,j))
dir = flip_dir(dir)
cur_sym = input[i][j]

count=0
while(cur_sym != 'S'):
    i, j, dir = traverse(i, j, dir, cur_sym)
    loop_indices.append((i,j))
    dir = flip_dir(dir)
    cur_sym = input[i][j]
    count+=1

# inside_loop=False
# line_num=0
# for line in area_input:
#     char_num=0
#     for char in line:
#         if (line_num, char_num) in loop_indices:
#             if not inside_loop:
#                 inside_loop=True
#         else:


#         char_num+=1
#     line_num+=1

import matplotlib.pyplot as plt
from matplotlib.path import Path
out=0
p = Path(loop_indices)
# for y in range(len(input)):
#     for x in range(len(input[0])):
#         if (x, y) in loop_indices:
#             continue
#         if p.contains_point((x, y)):
#             out+=1
plt.plot(loop_indices)
plt.show()
print(out)
