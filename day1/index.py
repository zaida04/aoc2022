def accumulateElfCalories():
	overall = []
	file = open("input.txt", "r").readlines()

	acc = 0
	for line in file:
		if line == "\n":
			overall.append(acc)
			acc = 0
		else:
			acc += (int(line.rstrip("\n")))

	return overall

def main():
	calories = accumulateElfCalories()
	print(f"Max calories: {max(calories)}")

	calories.sort()
	total = calories[-1] + calories[-2] + calories[-3]
	print(f"Total calories from top 3: {total}")
	
main()
