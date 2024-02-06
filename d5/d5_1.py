f = open("input.txt", "r")
lines = f.readlines()
out=None

def process_input():
    i=-1
    input_list=[]
    temp_list=[]
    seeds=[]
    for line in lines:
        # first line
        if "seeds" in line:
            line = line.replace("seeds:", "")
            for sub in line.split(","):
                pair = list(map(int, sub.split()))
                seeds.append(pair)
        else:
            if line in ['\n', '\r\n']:
                if i!=-1:
                    input_list.append(temp_list)
                    temp_list = []
                i+=1
                continue
            if not "map" in line:
                temp_list.append(list(map(int, line.strip().split())))

    return (input_list, seeds)
    
def get_d_s_ranges(line):
    return ((line[0], line[0] + line[2]-1), (line[1], line[1] + line[2]-1))

def is_seed(val, seeds):
    for line in seeds:
        if seed_in_range(val, line):
            return True
    return False    
    
def seed_in_range(val, line):
    if val>=line[0] and val<line[0]+line[1]:
        return True
    else:
        return False

def is_in_source_range(val, line):
    if val>=line[1] and val<line[1]+line[2]:
        return True
    else:
        return False

def get_line_dest(val, line):
    diff = line[0]-line[1]
    return val+diff

def get_list_dest(val, list):
    for line in list:
        if is_in_source_range(val, line):
            return get_line_dest(val, line)
    return val

def is_in_dest_range(val, line):
    if val>=line[0] and val< line[0]+line[2]:
        return True
    else:
        return False
    
def get_line_source(val, line):
    diff=line[1]-line[0]
    return val+diff

def get_list_source(val, list):
    for line in list:
        if is_in_dest_range(val, line):
            return get_line_source(val, line)
    return val

(input_list, seeds) = process_input()

i=-1
while(i<20000000000):
    i+=1
    func_num=6
    cur_val=i
    while(func_num>=0):
        cur_val = get_list_source(cur_val, input_list[func_num])
        func_num-=1

    if is_seed(cur_val, seeds):
        out=i
        break

print(out)