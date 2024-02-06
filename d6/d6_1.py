input=[[59, 543], [68, 1020], [82, 1664], [74, 1022]]
out=1

def calc_dist(time_held, race):
    return time_held*(race[0]-time_held)

for race in input:
    cur_counter=0
    for i in range(race[0]+1):
        if calc_dist(i, race) > race[1]:
            cur_counter+=1

    out*=cur_counter

print(out)

