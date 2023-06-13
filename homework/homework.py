inp = input()

inp = inp.split(";")
total = 0

for el in inp:
  if "-" in el:
    el = el.split("-")
    inp = [int(ell) for ell in el]
    total += inp[1] - inp[0] + 1
  else:
    total += 1

print(total)

