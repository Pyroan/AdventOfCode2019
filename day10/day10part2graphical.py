import tkinter as tk
from time import sleep
# Let's try a little something new.
field = []
with open('day10.txt') as f:
    for line in f:
        field.append(list(line.strip()))

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)

def update_frame():
    f =''
    for l in field:
        f += ' '.join(l) + '\n'
    text.insert(1.0,f)
    if winner != '':
        text.tag_add('winner', winner)
        text.tag_configure('winner', foreground='#23cc2b')
    text.tag_add('ship', '{}.{}'.format(y+1,x*2))
    text.tag_configure('ship', foreground='#e60000')
    if laser != []:
        for c in laser:
            text.tag_add('laser','{}.{}'.format(c[0],c[1]))
        text.tag_configure('laser', foreground='#e60000')
    root.update_idletasks()
    root.update()

root = tk.Tk(screenName="Day 10")
text = tk.Text(root, width=len(field[0])*2, height=len(field), font =('Fira Code', 12), bg='#01000f', fg='#e0dff0')
text.pack()

winner = ''
laser = []

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
field[y][x]='X'
vaporized = 0

s = slopes.index((-1,0))
i,j = 0,0
#while vaporized < 200:
while '#' in ''.join([''.join(line) for line in field]):
    slope = slopes[s]
    # Cast ray
    laser = []
    i,j = y,x
    while 0 <= i+slope[0] <= max_v and 0 <= j+slope[1] <= max_h:
        i += slope[0]
        j += slope[1]
        laser.append((i+1, j*2))
        if field[i][j] == '#':
            vaporized += 1
            if vaporized == 200:
                field[i][j] = 'O'
                winner = '{}.{}'.format(i+1,j*2)
            else:
                field[i][j] = '.'
            break
        elif field[i][j] != 'O':
            field[i][j] = 'X'
        update_frame()
    # Unrender laser
    for l in laser:
        if field[l[0]-1][l[1]//2] == 'X':
            field[l[0]-1][l[1]//2] = '.'
    s = (s+1) % len(slopes)

print(j*100+i)
    
while True:
    update_frame()