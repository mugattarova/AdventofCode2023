def is_a_gear(c):
    if c == '*':
        return True
    else:
        return False
    
def get_number(line_arr, num_i):
    #if index is 
    num_str = line_arr[num_i]
    i=1
    while (num_i+i<140 and num_i+i>-1) and line_arr[num_i+i].isdigit():
        num_str=num_str+line_arr[num_i+i]
        i+=1

    i=-1
    while (num_i+i<140 and num_i+i>-1) and line_arr[num_i+i].isdigit():
        num_str=line_arr[num_i+i]+num_str
        i-=1
    
    return int(num_str)

def is_left_digit(line_arr, num_i):
    if num_i-1<0:
        return False
    elif line_arr[num_i-1].isdigit():
        return True
    else:
        return False

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

for line_num in range(0, 140):
    line_arr = input[line_num]

    for char_num in range(0, 140):
        char = line_arr[char_num]
        if(line_num==1 and char_num==19):
            print("here")

        if is_a_gear(char):
            adj_nums = []
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if (char_num+i<140 and line_num+j<140) and (char_num+i>-1 and line_num+j>-1) and input[line_num+i][char_num+j].isdigit():
                        if j==-1:
                            adj_nums.append(get_number(input[line_num+i], char_num+j))
                        # if part of a number, don't count
                        elif is_left_digit(input[line_num+i], char_num+j):
                            continue
                        else:
                            adj_nums.append(get_number(input[line_num+i], char_num+j))

            if len(adj_nums) == 2:
                out+= adj_nums[0]*adj_nums[1]
                            
print(out)