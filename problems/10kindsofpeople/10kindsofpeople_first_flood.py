from collections import deque

string_to_nums = lambda s: [int(e) for e in s.split(" ")]

def all_reachable(map, start, hr, hc):
    type = map[start[0]][start[1]]
    Q = deque([start])
    visited = set()
    while len(Q) != 0:
        r, c = at = Q.pop()
        for (mr, mc) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nr, nc = new = r + mr, c + mc
            if new not in visited and nc >= 0 and nr >= 0 and nc <= hc and nr <= hr and map[nr][nc] == type:
                Q.append(new)
                visited.add(new)
    return visited

def in_sets(what, sets):
    for set in sets:
        if what in set:
            return True
    return False

def do_query(query, seas):
    start, end = query
    for sea in seas:
        if start in sea:
            if end in sea:
                return True
            else:
                return False

import time
start_time = time.time()

r, c = string_to_nums(input())
map = []
for ign in range(r):
    map.append([int(e) for e in input()])
n = int(input())
queries = []
for ign in range(n):
    r1, c1, r2, c2 = string_to_nums(input())
    queries.append(((r1 - 1, c1 - 1), (r2 - 1, c2 - 1)))

#make big
for row in map:
    row += row * 49
map += map * 2
queries += queries * 249
print(len(map), len(map[0]), len(queries))
r, c = len(map), len(map[0])

seas = []

for tr in range(r):
    for tc in range(c):
        at = tr, tc
        if in_sets(at, seas):
            continue
        seas.append(all_reachable(map, at, r-1, c-1))

print("seas done", time.time() - start_time)

for query in queries:
    if do_query(query, seas) == True:
        type = map[query[0][0]][query[0][1]]
        #print(["binary", "decimal"][type])
        pass
    else:
        #print("neither")
        pass

print("done", time.time() - start_time)
