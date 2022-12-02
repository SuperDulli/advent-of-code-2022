lines = open("input", "r").read()[:-1].split("\n")

# A, X => Rock
# B, Y => Paper
# C, Z => Siccors


def shape_score(shape):
	if shape == "X":
		return 1
	elif shape == "Y":
		return 2
	elif shape == "Z":
		return 3
	else:
		raise ValueError

def outcome_score(opponent, player):
	if opponent == "A":
		if player == "Z":
			return 0
		elif player == "Y":
			return 6
		else:
			return 3
	elif opponent == "B":
		if player == "X":
			return 0
		elif player == "Z":
			return 6
		else:
			return 3
	elif opponent == "C":
		if player == "Y":
			return 0
		elif player == "X":
			return 6
		else:
			return 3
	else:
		return 0

score = 0
for line in lines:
	score += shape_score(line[2]) + outcome_score(line[0], line[2])

print(score)
