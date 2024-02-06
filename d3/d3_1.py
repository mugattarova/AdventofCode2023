import numpy as np

def is_a_part(c):
    c=c.strip()
    if c == '.':
        return False
    elif c.isdigit():
        return False
    elif c is None:
        return False
    else:
        return True

def process_input():
    f = open("input3.txt", "r")
    lines = f.readlines()
    # input = np.chararray((140, 140))
    # i_input_process=0
    # for line in lines:
    #     line = line.rstrip()
    #     line_arr = list(line)
    #     j_input_process=0
    #     for char in line_arr:
    #         input[i_input_process][j_input_process] = char
    #         j_input_process+=1
    #     i_input_process+=1
    input = []
    for line in lines:
        line = line.rstrip()
        input.append(list(line))

    return input

out=0
input=process_input()
# input processed

for line_num in range(0, 140):
    line_arr = input[line_num]
    num_str=""
    part_adj=False
    char_num=0
    for char in line_arr:
        if char.isdigit():
            num_str=num_str+char
            # iterate through neighbours
            # set part_adj=True
            # input[char.index, j] - self
            for n in range(-1,2):
                for m in range(-1, 2):
                    if not (n==0 and m==0):
                        if (char_num+n<140 and line_num+m<140) and (char_num+n>-1 and line_num+m>-1) and is_a_part(input[line_num+m][char_num+n]):
                            part_adj=True
            #if next char is not a digit, or this char is last
            if char_num==139 or not line_arr[char_num+1].isdigit():
                if num_str != "" and part_adj==True:
                    out+=int(num_str)
                num_str=""
                part_adj=False
        char_num+=1

print(out)