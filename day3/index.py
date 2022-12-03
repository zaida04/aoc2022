import string
chars = string.ascii_lowercase + string.ascii_uppercase
f = list(map(lambda x: x.strip(), open("input.txt", "r").readlines()))

## Part 1

total = 0
for line in f:
  halfLen = len(line) // 2
  seg1 = line[0:halfLen]
  seg2 = line[halfLen:]

  cached = []
  for char in seg1:
    if(char in cached): continue
    if(seg2.find(char) != -1):
      total += chars.index(char) + 1
      break 

print(f"[Part1]: {total}")

## Part 2

second_total = 0
for index in range(0, len(f), 3):
  g1, g2, g3 = f[index:index+3]

  cached = []
  for char in g1:
    if(char in cached): continue
    if(g2.find(char) != -1 and g3.find(char) != -1):
      second_total += chars.index(char) + 1
      break 
    cached.append(char)

print(f"[Part2]: {second_total}")
