file = open("input", "r")
lines = file.readlines()

# Part 1 - find largest sum
sums = []
calories = 0
for line in lines:
	if line == "\n":
		sums.append(calories)
		calories = 0
	else:
		calories += int(line)
print(max(sums))

# Part 2 - find sum of the three largest sum
sums.sort(reverse=True)
print(sum(sums[:3]))
