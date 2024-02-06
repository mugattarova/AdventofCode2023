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

instruct, nodes = process_input()
out = 0
cur_node = "AAA"
while cur_node != "ZZZ":
    for step in instruct:
        cur_node = take_route(cur_node, step, nodes)
        out+=1
        if cur_node == "ZZZ":
            break

print(out)