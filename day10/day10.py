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
slopes = set([(a//gcd(a,b),b//gcd(a,b)) for a in range(1,max_v+1) for b in range(1,max_h+1)])
slopes.add((0,1))
slopes.add((1,0))
# print(slopes)
for y in range(len(field)):
    for x in range(len(field[y])):
        if field[y][x] != '#':
            continue
        detected = set()
        # SWEEP
        # 0-90 degrees
        for slope in slopes:
            # Cast ray
            i,j = y,x
            while i+slope[0] <= max_v and j+slope[1] <= max_h:
                try:
                    i += slope[0]
                    j += slope[1]
                    if field[i][j] == '#':
                        detected.add((j,i))
                        break
                except IndexError as e:
                    print(e, [j,i])
            # Cast ray in opposite direction
            i,j = y,x
            while i-slope[0] >= 0 and j-slope[1] >= 0:
                i -= slope[0]
                j -= slope[1]
                if field[i][j] == '#':
                    detected.add((j,i))
                    break
            # # Cast ray in inverse direction
            i,j = y,x
            while i+slope[0] <= max_v and j-slope[1] >= 0:
                i += slope[0]
                j -= slope[1]
                if field[i][j] == '#':
                    detected.add((j,i))
                    break

            # # Cast ray in inverse opposite direction
            i,j = y,x
            while i-slope[0] >= 0 and j+slope[1] <= max_h:
                i -= slope[0]
                j += slope[1]
                if field[i][j] == '#':
                    detected.add((j,i))
                    break

        if len(detected) >= biggest:
            biggest = len(detected)
            biggest_loc = [x,y]
        
        # print([x,y], '->', len(detected))
        

print(biggest)
print(biggest_loc)
