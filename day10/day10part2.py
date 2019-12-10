# Lowkey raytracing.
field = []
with open('day10.txt') as f:
    for line in f:
        field.append(list(line.strip()))

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)

biggest = 0
biggest_loc = []

max_v = len(field)-1
max_h = len(field[0])-1
# MAKE SLOPES BIGGERERRRRRRRRR
quadrants = []
slopes = set([(a//gcd(a,b),b//gcd(a,b)) for a in range(1,max_v+1) for b in range(1,max_h+1)])
slopes = sorted(list(slopes), key=lambda x: x[0]/x[1], reverse=True)
slopes.insert(0, (1,0))
slopes.append((0,1))
quadrants.append(slopes)
# append same, but reversed and with y values flipped
quadrants.append(list(reversed([(-s[0], s[1]) for s in slopes[:-1]])))
# append same, but forward and with x and y values flipped?
quadrants.append([(-s[0], -s[1]) for s in slopes[1:]])
# append same, but reversed and with x values flipped.
quadrants.append(list(reversed([(s[0], -s[1]) for s in slopes[:-1]])))
slopes = quadrants[0]+quadrants[1]+quadrants[2]+quadrants[3][:-1] # idek
slopes.reverse()

x,y = 23,20 # answer from part 1 don't judge me.
vaporized = 0

s = slopes.index((-1,0))
i,j = 0,0
while vaporized < 200:
    slope = slopes[s]
    # Cast ray
    i,j = y,x
    while 0 <= i+slope[0] <= max_v and 0 <= j+slope[1] <= max_h:
        i += slope[0]
        j += slope[1]
        if field[i][j] == '#':
            field[i][j] = '.'
            vaporized += 1
            break
    
    s = (s+1) % len(slopes)

print(j*100+i)
        

