def read_file(file_name):
	with open(file_name, "r") as f:
		data = f.read().splitlines()
	return data

EXAMPLE_FILE = "example"
INPUT_FILE = "input"
directions = [(0,1), (0,-1), (1,0), (-1,0)]
example_trees = list(read_file(EXAMPLE_FILE))
trees = list(read_file(INPUT_FILE))

def is_visible(trees, x, y, x_max, y_max):
	tree = int(trees[y][x])
	for direction in directions:
		i,j = x,y
		i_,j_ = direction
		i += i_
		j += j_
		visible = 1
		while visible == 1 and 0 <= i and i < x_max and 0 <= j and j < y_max:
			if int(trees[j][i]) >= tree:
				visible = 0
			i += i_
			j += j_
		if visible == 1:
			return 1
	return 0

def check_visiblities(trees):
	visible_matrix = []
	for y,line in enumerate(trees):
		row = []
		if y == 0 or y == len(trees) - 1:
			visible_matrix.append([1] * len(trees))
			continue
		for x,tree in enumerate(line):
			if x == 0 or x == len(line) - 1:
				row.append(1)
			else:
				# print(x, y, tree, is_visible(trees, x, y, len(line), len(trees)))
				row.append(is_visible(trees, x, y, len(line), len(trees)))
		visible_matrix.append(row[:])
	return visible_matrix

def solve_part1(trees):
	visible_matrix = check_visiblities(trees)
	count = 0
	for line in visible_matrix:
		for tree in line:
			if tree == 1:
				count += 1
	return count

print("## Part 1 ##")
print(solve_part1(example_trees))
print(solve_part1(trees))

def scenic_score(trees, x, y, x_max, y_max):
	score = 1
	tree = int(trees[y][x])
	for direction in directions:
		i,j = x,y
		i_,j_ = direction
		i += i_
		j += j_
		visible = 0
		blocked = False
		while not blocked and 0 <= i and i < x_max and 0 <= j and j < y_max:
			visible += 1
			if int(trees[j][i]) >= tree:
				blocked = True
			i += i_
			j += j_
		score *= visible
	return score


def check_score(trees):
	score_matrix = []
	for y,line in enumerate(trees):
		row = []
		if y == 0 or y == len(trees) - 1:
			score_matrix.append([0] * len(trees))
			continue
		for x,tree in enumerate(line):
			if x == 0 or x == len(line) - 1:
				row.append(0)
			else:
				row.append(scenic_score(trees, x, y, len(line), len(trees)))
		score_matrix.append(row[:])
	return score_matrix


def solve_part2(trees):
	scores = check_score(trees)
	maximum = 0
	for line in scores:
		m = max(line)
		if m > maximum:
			maximum = m
	return maximum

print("## Part 2 ##")
print(solve_part2(example_trees))
print(solve_part2(trees))
