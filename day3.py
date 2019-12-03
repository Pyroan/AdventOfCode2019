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
# Two lines A and B intersect if...
# A is horizontal and B is vertical:
#    Possible intersection i is given by (B.x, A.y)
#    i is valid iff  (A.x1 <= i.x <= A.x2 OR A.x1 >= i.x >= A.x2)
#        AND (B.y1 <= i.y <= B.y2 OR B.y1 >= i.y >= B.y2)
# A and B are both horizontal:
#   if A.y == B.y, possible intersections are the overlap of the x components.
# A and B are vertical:
#   same as if they're horizontal but flip x's and y's

# Save all intersections as points
intersections = []
def add_hv_intersection(hz, vt):
    i = (vt[0][0], hz[0][1])
    if i == (0,0): 
        return
    # READABLE. CODE.
    if i[0] in range(min(hz[0][0], hz[1][0]),max(hz[0][0],hz[1][0]) + 1):
        if i[1] in range(min(vt[0][1], vt[1][1]), max(vt[0][1], vt[1][1]) + 1):
            intersections.append(i)

def add_hz_intersections(a, b):
    if a[0][1] != b[0][1]:
        return
    print('blorp')
    pass
def add_vt_intersections(a, b):
    if a[0][0] != b[0][0]:
        return
    print('zorp')
    pass

def is_horizontal(ln):
    return ln[0][1] == ln[1][1]
def is_vertical(ln):
    return ln[0][0] == ln[1][0]

for a in wires[0]:
    for b in wires[1]:
        if is_horizontal(a) and is_vertical(b):
            add_hv_intersection(a, b)
        elif is_horizontal(b) and is_vertical(a):
            add_hv_intersection(b, a)
        elif is_horizontal(a) and is_horizontal(b):
            add_hz_intersections(a,b)
        elif is_vertical(a) and is_vertical(b):
            add_vt_intersections(a,b)
        
# Find intersection with smallest x + y   
print(min([abs(pt[0]) + abs(pt[1]) for pt in intersections]))

# Turns out I got really lucky and the horizontal/vertical cases didn't matter, even though there WAS a horizontal overlap in my map