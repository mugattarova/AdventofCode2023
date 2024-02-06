f = open("input.txt", "r")
lines = f.readlines()
out=0

# gen input
def process_input():
    win_cards = []
    your_cards = []
    for line in lines:
        line = line.rstrip()
        line = line.replace(":", "")
        line = line.replace("Card", "")
        win_nums_str, your_nums_str = line.split("|")

        win_nums = list(map(int, win_nums_str.split()))
        win_nums.pop(0)
        win_cards.append(win_nums)
        your_nums = list(map(int, your_nums_str.split()))
        your_cards.append(your_nums)

    return (win_cards, your_cards)

win_cards, your_cards = process_input()
dupl_count = [1] * 219

line_count = 0
while line_count < len(win_cards):
    cur_win_nums = win_cards[line_count]
    cur_your_nums = your_cards[line_count]
    cur_win_count = 0

    # find matches
    for num in cur_your_nums:
        if num in cur_win_nums:
            cur_win_count+=1

    # write dupl
    for i in range(dupl_count[line_count]):
        for j in range(cur_win_count):
            dupl_count[line_count+j+1]+=1
    
    line_count+=1

print(sum(dupl_count))
# 👍