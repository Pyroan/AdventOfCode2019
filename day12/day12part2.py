from itertools import combinations
from math import gcd
moons = [] 
with open('day12.txt') as f:
    for line in f.readlines():
        moon = {}
        pos = line.strip().split(', ')
        moon['position'] = []
        moon['position'].append(int(pos[0][3:]))
        moon['position'].append(int(pos[1][2:]))
        moon['position'].append(int(pos[2][2:-1])) 
        moon['velocity'] = [0,0,0]
        moons.append(moon)

# Return a string representing all values of the x,y, or z component
def value(component):
    p = ','.join([str(moon['position'][component]) for moon in moons])
    v = ','.join([str(moon['velocity'][component]) for moon in moons])
    return ':'.join([p,v])

# Lengths of the sequences for each set of X, Y, and Z components.
seqs = [1]*3 # stop giggling.
stopseq =[False]*3
states = [value(i) for i in range(3)]
print(states)
while True:
    pairs = combinations(moons, 2)
    
    # Apply gravity.
    for pair in pairs:
        m,n = pair[0], pair[1]
        for i in range(3):
            if stopseq[i]:
                continue
            if m['position'][i] < n['position'][i]:
                m['velocity'][i] += 1
                n['velocity'][i] -= 1
            elif m['position'][i] > n['position'][i]:
                m['velocity'][i] -= 1
                n['velocity'][i] += 1
            else:
                m['velocity'][i] += 0
                n['velocity'][i] += 0

    # Apply velocity.
    for moon in moons:
        moon['position'][0] += moon['velocity'][0]
        moon['position'][1] += moon['velocity'][1]
        moon['position'][2] += moon['velocity'][2]
    
    # Detect complete sequences
    for i in range(3):
        if not stopseq[i]:
            if states[i] == value(i):
                stopseq[i] = True
                print("stopping", i)
            else:
                seqs[i] += 1
    if False not in stopseq:
        break


# Calculate lowest common multiple
# (stolen from SO)
lcm = seqs[0]
for i in seqs[1:]:
    lcm = lcm*i//gcd(lcm,i)
print(lcm)