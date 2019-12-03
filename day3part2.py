ins = []
with open('day3.txt') as f:
    for line in f.readlines():
        ins.append(line.split(','))
# Instead of mapping wires, just list them as pairs of points.
wires = []
for j in range(len(ins)):
    ptr = [0,0]
    lines = []
    for i in ins[j]:
        new_ptr = ptr[:]
        if i[0] == 'R':
            new_ptr[0] += int(i[1:])
        elif i[0] == 'L':
            new_ptr[0] -= int(i[1:])
        elif i[0] == 'U':
            new_ptr[1] += int(i[1:])
        elif i[0] == 'D':
            new_ptr[1] -= int(i[1:])    
        
        lines.append([tuple(ptr), tuple(new_ptr)])
        ptr = new_ptr[:]
    wires.append(lines)

# Save all intersections as points
intersections = []
def add_hv_intersection(hz, vt):
    i = (vt[0][0], hz[0][1])
    if i == (0,0): 
        return False
    # READABLE. CODE.
    if i[0] in range(min(hz[0][0], hz[1][0]),max(hz[0][0],hz[1][0]) + 1):
        if i[1] in range(min(vt[0][1], vt[1][1]), max(vt[0][1], vt[1][1]) + 1):
            intersections.append(i)
            return True
    return False

def is_horizontal(ln):
    return ln[0][1] == ln[1][1]
def is_vertical(ln):
    return ln[0][0] == ln[1][0]

step_totals = []
for i in range(len(wires[0])):
    for j in range(len(wires[1])):
        a = wires[0][i]
        b = wires[1][j]
        if is_horizontal(a) and is_vertical(b):
            intersected = add_hv_intersection(a, b)
        elif is_horizontal(b) and is_vertical(a):
            intersected = add_hv_intersection(b, a)
        else:
            intersected = False
        
        # This is dumb and lazy but fight me.
        if intersected:
            # Get length of all completed lines up to this point
            steps = sum([int(x[1:]) for x in ins[0][:i]] + [int(x[1:]) for x in ins[1][:j]])
            # Add length for partial segments
            n = intersections[-1] # most recent intersection shut up.
            steps += abs(n[1] - a[0][1]) + abs(n[0] - a[0][0])
            steps += abs(n[1] - b[0][1]) + abs(n[0] - b[0][0])
            step_totals.append(steps)

print(min(step_totals))
# Still lucky. This worked first try too, which is ridiculous.