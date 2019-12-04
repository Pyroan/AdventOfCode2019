def contains_adjacent(n):
    seqlen = 1
    for i in range(len(n)-1):
        if n[i] == n[i+1]:
            seqlen += 1
        else:
            if seqlen == 2:
                return True
            seqlen = 1
    if seqlen == 2:
        return True # shut up shut up shut up
    return False

def decreases(n):
    for i in range(len(n)-1):
        if n[i] > n[i+1]:
            return True
    return False


with open('day4.txt') as f:
    x = f.readline().split('-')
    r = range(int(x[0]), int(x[1]))

count = 0
for i in r:
    l = list(map(int,str(i)))
    if contains_adjacent(l) and not decreases(l):
        count += 1
print(count)