f = open("input.txt", "r")
lines = f.readlines()
out=0

for line in lines:
    line = line.rstrip()
    line = line.replace(":", "")
    line = line.replace("Card", "")
    win_nums_str, your_nums_str = line.split("|")

    win_nums = list(map(int, win_nums_str.split()))
    your_nums = list(map(int, your_nums_str.split()))
    card_num = win_nums.pop(0)
    win_count = 0

    for num in your_nums:
        if num in win_nums:
            win_count+=1

    if win_count!=0:
        out+=pow(2, win_count-1)
        win_count = 0

print(out)
