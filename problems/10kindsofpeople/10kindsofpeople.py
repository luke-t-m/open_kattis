from collections import deque

# TODO: Rewrite in C++

string_to_nums = lambda s: [int(e) for e in s.split(" ")]
in_bounds = lambda r, c: r < height and r >= 0 and c < width and c >= 0
tuplecords = lambda c, grid: grid[c[0]][c[1]]

def get(map, r, c):
    if in_bounds(r, c):
        return map[r][c]
    
def set(map, r, c, val):
    if in_bounds(r, c):
        map[r][c] = val

def flood(map):
    lastsegs = [0, 1]
    Q = deque()
    for r in range(height):
        for c in range(width):
            seg = get(map, r, c)
            if seg <= 1:
                lastsegs[seg] += 2
                nseg = lastsegs[seg]
                Q.append((r, c))
                while len(Q) != 0:
                    at = Q.pop()
                    ar, ac = at
                    pseg = get(map, ar, ac)
                    if pseg != seg:
                        continue
                    set(map, ar, ac, nseg)
                    Q.extend([(ar - 1, ac), (ar, ac + 1), (ar + 1, ac), (ar, ac - 1)])


#input
height, width = string_to_nums(input())
map = []
for ign in range(height):
    map.append([int(e) for e in input()])
n = int(input())
queries = []
for ign in range(n):
    r1, c1, r2, c2 = string_to_nums(input())
    start = (r1 -1, c1 -1)
    end = (r2 - 1, c2 - 1)
    queries.append((start, end))

#make big (for testing)
if 0:
    for row in map:
        row += row * 49
    map += map * 99
    queries += queries * 333
    print(len(map), len(map[0]), len(queries))
    r, c = len(map), len(map[0])

flood(map)

for query in queries:
    start, end = query
    if (type := tuplecords(start, map)) == tuplecords(end, map):
        print(["binary", "decimal"][type % 2])
    else:
        print("neither")