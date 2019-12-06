with open('day6.txt') as f:
    guide = [s.strip().split(')') for s in f.readlines()]


# A satellite has as many orbits as its depth in the tree
# So sum of the depths in the tree i suppose
tree = {}
# Build tree
for edge in guide:
    if edge[0] not in tree.keys():
        tree[edge[0]] = []
    tree[edge[0]].append(edge[1])

# Traverse tree and sum depths
def orbits(node, depth):
    total = 0
    if node not in tree.keys():
        return depth
    return total + depth + sum([orbits(n, depth+1) for n in tree[node]])

print(orbits('COM', 0))

# In part two I build the tree backwards and part 1 can prob be solved this way too,
# By summing the lenths of the paths