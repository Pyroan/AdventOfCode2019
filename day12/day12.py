from itertools import combinations
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

# print(moons)

for _ in range(1000):
    pairs = combinations(moons, 2)
    # Apply gravity.
    for pair in pairs:
        m,n = pair[0], pair[1]
        for i in range(3):
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
    #     print('pos={}, vel={}'.format(moon['position'], moon['velocity']))
    # print()

# Calculate Energy.
print(sum([sum(map(abs, m['position'])) * sum(map(abs, m['velocity'])) for m in moons]))