# reads one line from input "n a b c". Returns all possible orderings of n length of a, b and c objects (line specifies how many of each object) with all unique objects (LOLNO) and no two objects of the same type appearing consecutively.

from collections import deque

inp = input()
inp = inp.split(" ")
n, a, b, c = [int(el) for el in inp]
numdict = {"a": a, "b": b, "c": c}

class state:
  def __init__(self, tot, at, n):
    self.tot = tot
    self.at = at
    self.n = n

start = state(1, None, n)
Q = deque()
Q.append(start)

total = 0

while len(Q):
  c = Q.popleft()
  for pos in ["a", "b", "c"]:
    if pos == c.at:
      continue
    n = c.n - 1
    new_tot = c.tot * numdict[pos] 
    if n:
      new = state(new_tot, pos, n)
      Q.append(new)
    else:
      total += new_tot
       
print(total % (10 ** 9 + 7)) 
