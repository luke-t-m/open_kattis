class to_infinity():
    def __iter__(self):
        self.n = -1
        return self

    def __next__(self):
        self.n += 1
        return self.n
    
def range_to_inf():
    obj = to_infinity()
    return iter(obj)

def frog_it_up(n, s, m, squares):
  visited = set()

  for h in range_to_inf():
      if s < 0:
          return f"left\n{h}"
      if s >= n:
          return f"right\n{h}"
      if squares[s] == m:
          return f"magic\n{h}"
      if s in visited:
          return f"cycle\n{h}"
      visited.add(s)
      s += squares[s]


string_to_nums = lambda s: [int(e) for e in s.split(" ")]

n, s, m = string_to_nums(input())
squares = string_to_nums(input())

print(frog_it_up(n, s - 1, m, squares))
    

