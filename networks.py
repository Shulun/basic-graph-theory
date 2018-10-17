import math

def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    G[node1][node2] = 1
    if node2 not in G:
        G[node2] = {}
    G[node2][node1] = 1

# ring = {}
# n = 50

# for i in range(n):
#     make_link(ring, i, (i+1)%n)

# print(len(ring))
# print(sum([len(ring[node]) for node in ring.keys()])/2)
# print(ring)

grid = {}
n = 256
side = int(math.sqrt(n))

for i in range(side):
    for j in range(side):
        if i < side - 1: make_link(grid, (i, j), (i+1, j))
        if j < side - 1: make_link(grid, (i, j), (i, j+1))

print(len(grid))
print(sum([len(grid[node]) for node in grid.keys()])/2)
# print(grid)