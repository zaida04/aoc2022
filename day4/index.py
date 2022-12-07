f = open("input.txt", "r").readlines()

count_1 = 0
count_2 = 0
for line in f:
  splitPairs = line.rstrip("\n").split(",")
  ranges = [int(item) for x in [x.split("-") for x in splitPairs] for item in x]

  (r1, r2, r3, r4) = ranges
  # Part 1
  if (r3 >= r1 and r4 <= r2) or (r3 <= r1 and r4 >= r2):
    count_1 += 1

  # Part 2
  if (r3 >= r1 and r3 <= r2) or (r4 >= r1 and r4 <= r2) or (r1 >= r3 and r1 <= r4) or (r2 >= r3 and r2 <= r4):
    count_2 += 1

print(f"[Part1]: {count_1}")
print(f"[Part2]: {count_2}")
