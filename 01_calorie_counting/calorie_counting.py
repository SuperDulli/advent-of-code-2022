file = open("input", "r")
lines = file.readlines()

sums = []
calories = 0
for line in lines:
	if line == "\n":
		sums.append(calories)
		calories = 0
	else:
		calories += int(line)

print(max(sums))
