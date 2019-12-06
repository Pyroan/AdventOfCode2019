with open('day6.txt') as f:
    guide = [s.strip().split(')') for s in f.readlines()]

tree = {}
# Build tree backwards so each node is pointing to its parent
for edge in guide:
    tree[edge[1]] = edge[0]

# Get path from root to node
def get_path(root, node):
    path = []
    while node != root:
        path.append(node)
        node = tree[node]
    path.append(node)
    return list(reversed(path))

you = get_path('COM', 'YOU')
san = get_path('COM', 'SAN')
# Chop off common path
for i in range(max(len(you), len(san))):
    if you[i] != san[i]:
        you = you[i:]
        san = san[i:]
        break

print(len(you)+len(san)-2)