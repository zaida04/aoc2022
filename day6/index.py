f = open("index.txt", "r").readlines()[0]   

def has_duplicate(str):
  if not len(str): return False
  if str[0] in str[1:]: return True
  return has_duplicate(str[1:])

def findEndOfMarker(increment):
  for i in range(0, len(f)):
    chars = f[i:i+increment]
    if not has_duplicate(chars): 
      return i + increment


partOneIndex = findEndOfMarker(4)
partTwoIndex = findEndOfMarker(14)

print(f"[Part1]: {partOneIndex}")
print(f"[Part2]: {partTwoIndex}")

