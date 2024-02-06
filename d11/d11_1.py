def process_input() -> list:
    f = open("input", "r")
    lines = f.readlines()
    input=[]
    for line in lines:
        temp = list(line.rstrip())
        if not "#" in temp:
            temp = [" "] * len(temp)
        input.append(temp)
    return input

def expand_universe_columns(input: list) -> list:
    j=0
    while j < len(input[0]):
        galaxy_found=False
        for line in input:
            if line[j] == "#":
                galaxy_found=True
                break
        if not galaxy_found:
            for line in input:
                line[j] = " "
        j+=1    
    return input

def print_universe(input: list):
    for line in input:
        print(''.join(line))
    print(" ")

def find_galaxies(input: list):
    galaxies_list=[]
    for line_num in range(len(input)):
        for char_num in range(len(input[0])):
            if input[line_num][char_num] == "#":
                galaxies_list.append((line_num, char_num))
    return galaxies_list

def all_empty(l:list):
    for e in l:
        if e != " ":
            return False
    return True

def find_distance(x, y, i, j, input) -> int:
    # line numbers
    upper_bound = max(x, i)
    lower_bound = min(x, i)
    vertical=[]
    # column
    for line in input[lower_bound:upper_bound]:
        vertical.append(line[y])
    # index in line numbers
    upper_bound = max(y, j)
    lower_bound = min(y, j)
    # row
    horizontal = input[x][lower_bound:upper_bound]

    h_dist=0
    v_dist=0
    expan_rate=1000000
    
    if(all_empty(vertical)):
        v_dist = len(vertical)
    else:
        empties = vertical.count(" ")
        v_dist = int(empties*expan_rate + len(vertical)-empties)
        # for v in range(len(vertical)):
        #     if vertical[v] == " ":
        #         v_dist+=expan_rate
        #     else:
        #         v_dist+=1

    if(all_empty(horizontal)):
        h_dist = len(horizontal)
    else:
        empties = horizontal.count(" ") 
        h_dist = int(empties*expan_rate + len(horizontal)-empties)
        # for h in range(len(horizontal)):
        #     if horizontal[h] == " ":
        #         h_dist+=expan_rate
        #     else:
        #         h_dist+=1

    return h_dist + v_dist

# --------- main ----------- #
input = expand_universe_columns(process_input())
galaxies=find_galaxies(input)
out=0

print("galaxies found: " + str(len(galaxies)))

for iter in range(len(galaxies)):
    x, y = galaxies[iter]
    for inner in range(iter+1, len(galaxies)):
        i, j = galaxies[inner]
        out+=find_distance(x, y, i, j, input)

print(out)