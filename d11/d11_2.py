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
