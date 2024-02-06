f = open("input1_1.txt", "r")
lines = f.readlines()
outSum = 0

for line in lines:
    chars = list(line.rstrip())
    numList = []
    first = None
    last = None
    currentString = ""

    # find first digit
    for c in chars:
        if(c.isdigit()):
            first = int(c)
        else:
            currentString += c

            if "one" in currentString:
                first = 1
            elif "two" in currentString:
                first = 2
            elif "three" in currentString:
                first = 3
            elif "four" in currentString:
                first = 4
            elif "five" in currentString:
                first = 5
            elif "six" in currentString:
                first = 6
            elif "seven" in currentString:
                first = 7
            elif "eight" in currentString:
                first = 8
            elif "nine" in currentString:
                first = 9

        if first is not None:
            break
            
    currentString = ""
    chars.reverse()

    # last digit
    for c in chars:
        if(c.isdigit()):
            last = int(c)
        else:
            currentString = c + currentString

            if "one" in currentString:
                last = 1
            elif "two" in currentString:
                last = 2
            elif "three" in currentString:
                last = 3
            elif "four" in currentString:
                last = 4
            elif "five" in currentString:
                last = 5
            elif "six" in currentString:
                last = 6
            elif "seven" in currentString:
                last = 7
            elif "eight" in currentString:
                last = 8
            elif "nine" in currentString:
                last = 9

        if last is not None:
            break

    val = int(first)*10 + int(last)
    outSum += val

print(outSum)
