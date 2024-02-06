def process_input():
    f = open("test", "r")
    lines = f.readlines()
    input=[]
    for line in lines:
        temp = list(map(int, line.rstrip().split()))
        input.append(temp)
    return input

def predict(vals: list[int]) -> int:
    if all_zeros(vals):
        return 0
    diff_list=[]
    for i in range(len(vals)-1):
        diff_list.append(diff(vals[i], vals[i+1]))
    return vals[0] - predict(diff_list)

def diff(v1: int, v2: int) -> int:
    return v2-v1

def all_zeros(l: list) -> bool:
    for e in l:
        if e != 0:
            return False
    return True

# ---------- Main ----------
input = process_input()
out=0
for line in input:
    out+=predict(line)

print(out)