import math as m

test=[71530, 940200]
input=[59688274, 543102016641022]
out=0

def calc_dist(time_held, race):
    return time_held*(race[0]-time_held)

race=input

top_bound = (race[0]+int(m.sqrt(race[0]**2 - 4*race[1])))/2

bot_bound = (race[0]-int(m.sqrt(race[0]**2 - 4*race[1])))/2

out = top_bound - bot_bound

print(out)

# time*total_time - time^2 > distance
# time^2 - time*total_time + distance < 0