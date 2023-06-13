inp = input()
inp = inp.split(" ")
wantlen, a, b, c = [int(el) for el in inp]

ca = cb = cc = 1
for i in range(wantlen - 1):
  na = b * cb + c * cc
  nb = a * ca + c * cc
  nc = a * ca + b * cb
  ca, cb, cc = na, nb, nc

total = a * ca + b * cb + c * cc
print(total % (10 ** 9 + 7))