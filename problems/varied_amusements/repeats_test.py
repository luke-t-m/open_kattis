from collections import deque

#wantlen = input("length of strings: ")
#wantlen = int(wantlen)
wantlen = 5
n1, n2, n3 = 1, 2, 3

full_guess = 3 ** wantlen
print(f"full_guess: {full_guess}")
bad_guess = 0
remaining_len, remaining_good = wantlen, full_guess
for ign in range(wantlen - 1):
  bad_guess += (full_guess - bad_guess) / 3
print(f"good_guess: {full_guess - bad_guess}")

Q = deque()
Q.append("")
full = []

while len(Q):
  x = Q.pop()
  if len(x) == wantlen:
    full.append(x)
  else:
    Q.extendleft([x + "a", x + "b", x + "c"])

genned = full

print(f"Length of full: {len(full)}")
good = [el for el in full if not("aa" in el or "bb" in el or "cc" in el)]
print(f"Length of good: {len(good)}")

bigstring = "".join(e for e in good)
for x in ["a", "b", "c"]:
  print(bigstring.count(x))

c = bigstring.count("a")

c_guess = len(good) * wantlen / 3 

print(f"C_GUESS!!! : {c_guess}")

for x in ["a", "b", "c"]:
  nos = [el.count(x) for el in good]
  for y in range(max(nos) + 1):
    print(f"no. {x} = {y}: {nos.count(y)}")


final = len(good)
no_repeats = 0
for n in [2, 2, 2]:
  final += (n - 1) * c
  c += ((n - 1) * c) / 2

print(final)

print("-"*20)


full = 3 ** wantlen
good = full * (2 / 3) ** (wantlen - 1)
good = int(good)
c = good * wantlen / 3
c = int(c)


print(full, good, c)

# WORKS FOR WANTLEN = 2, ALWAYS EXPECTED THIS. KEEP GOING.
oc = c
final = good
final += (n1 - 1) * c
c += (n1 - 1) * oc / 2
final += (n2 - 1) * c
c += (n2 - 1) * oc / 2
final += (n3 - 1) * c
print(final)

print("-"*20)
for_5 = [0, 16, 26, 4]

#for_5 = list(range(51))
#wantlen = 50

total = 0
for i in range(int(wantlen / 2) + 2):
  for j in range(int(wantlen / 2) + 2):
    for k in range(int(wantlen / 2) + 2):
      if i + j + k != wantlen: continue
      print(i, j, k)
      if i == 0:
        total += n2 * for_5[j] ** (j - 1) + n3 * for_5[k] ** (k - 1)
      elif j == 0:
        total += n1 * for_5[i] ** (i - 1) + n3 * for_5[k] ** (k - 1)
      elif k == 0:
        total += n1 * for_5[i] ** (i - 1) + n2 * for_5[j] ** (j - 1)
      else:
        total += n1 * for_5[i] ** (i - 1) + n2 * for_5[j] ** (j - 1) + n3 * for_5[k] ** (k - 1)

print(total)

print("-" * 20)

Q = deque()
Q.append("")
full = []

while len(Q):
  x = Q.pop()
  if len(x) == wantlen:
    full.append(x)
  else:
    Q.extendleft([x + "a", x + "b", x + "c"])

c1, c2, c3 = 2, 2, 1

subset = []
for x in full:
  if x.count("a") == c1 and x.count("b") == c2 and x.count("c") == c3:
    subset.append(x)

print(len(subset), subset)

good = [el for el in subset if not("aa" in el or "bb" in el or "cc" in el)]
print(len(good), good)

#full = 3 ** wantlen
good = len(subset) * (2 / 3) ** (wantlen - 1)
c = good * wantlen / 3

print(good, c)

print("-" * 20)

wantlen = 5
n1, n2, n3 = 1, 2, 3
n = n1 + n2 + n3

full = n ** wantlen

prob = 0
for nx in [n1, n2, n3]:
  prob += ((nx / n) ** 2)

a = (1 - (1/6 * 5/6)) ** 4
b = (1 - (1/3 * 2/3)) ** 4
c = (1 - (1/2 * 1/2)) ** 4
print(a, b, c)
prob = a + b + c - a * b - a * c - b * c + a * b * c
print(prob)
good = full * prob

good_real = full * 0.15278# for 5 1 2 3

print(full, good)

print("-" * 20)

wantlen = 1
n1, n2, n3 = 1, 2, 3

Q = deque()
Q.append("")
genned = []

while len(Q):
  x = Q.pop()
  if len(x) == wantlen:
    genned.append(x)
  else:
    Q.extendleft([x + "a", x + "b", x + "c", x + "d", x + "e", x + "f"])

reps = ["aa", "bb", "bc", "cb", "cc", "dd", "de", "df", "ed", "ee", "ef", "fd", "fe", "ff"]

good_genned = []

for el in genned:
  for rep in reps:
    if rep in el:
      break
  else:
    good_genned.append(el)

#print(good_genned)
#print("------")
#print(genned)
print("lengths of genned and good_genned:", len(genned), len(good_genned))

for x in ["a", "b", "c", "d", "e", "f"]:
  print(f"length of {x} starters: {len([el for el in good_genned if el[0] == x])}")

print(1296 * (22 / 36) ** 4)


print("-" * 20)

wantlen = 5

a, b, c = 1, 2, 3

ca = cb = cc = 1
for i in range(wantlen - 1):
  na = b * cb + c * cc
  nb = a * ca + c * cc
  nc = a * ca + b * cb
  ca, cb, cc = na, nb, nc
print(a * ca + b * cb + c * cc)

