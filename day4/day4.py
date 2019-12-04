def contains_adjacent(n):
    for i in range(len(n)-1):
        if n[i] == n[i+1]:
            return True
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

# 1liner if i have time
