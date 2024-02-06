import math
from functools import reduce

def process_input():
    f = open("input", "r")
    lines = f.readlines()
    i=0
    nodes={}
    for line in lines:
        if i==0:
            instruct = list(line.rstrip())
        else:
            temp_list = line.rstrip().replace("=", "").replace("(", "").replace(")", "").replace(",", "").split()
            nodes.update({temp_list[0]: (temp_list[1], temp_list[2])})
        i+=1
    return instruct, nodes

def take_route(node_name: str, inst: str, nodes: dict) -> str:
    (left, right) = nodes[node_name]
    if inst == 'L':
        return left
    if inst == 'R':
        return right
    return None

def find_start_nodes(nodes: dict) -> list:
    keys = nodes.keys()
    start_nodes = []
    for key in keys:
        key_letters = list(key)
        if key_letters[2] == "A":
            start_nodes.append(key)
    return start_nodes

def all_z(frontier: list) -> bool:
    non_z_last = False
    for node in frontier:
        letters = list(node)
        if letters[2] != "Z":
            non_z_last = True
            break
    if non_z_last == False:
        return True
    else:
        return False

def last_z(node: str) -> bool:
    letters = list(node)
    if letters[2]!="Z":
        return False
    else:
        return True
    
instruct, nodes = process_input()
frontier = find_start_nodes(nodes)
lcd = [0]*len(frontier)
out = 0

node_count=0
for node in frontier:
    while not last_z(node):
        for step in instruct:
            node = take_route(node, step, nodes)
            lcd[node_count]+=1
            if last_z(node):
                break
    node_count+=1

out=lcd[0]
for i in range(1, len(lcd)):
    out=math.lcm(out, lcd[i])
    
print(out)