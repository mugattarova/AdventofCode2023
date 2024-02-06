f = open("input1_1.txt", "r")
lines = f.readlines()
outSum = 0

for line in lines:
    chars = list(line)
    numList = []
    for c in chars:
        if(c.isdigit()):
            numList.append(c)

    first = numList.pop(0)
    if(len(numList) == 0):
        last = first
    else:
        last = numList.pop()

    val = int(first)*10 + int(last)
    outSum += val
    
print(outSum)
