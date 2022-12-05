def read_file(file_name):
	with open(file_name, "r") as f:
		data = f.read().splitlines()
	return data


EXAMPLE_FILE = "example"
INPUT_FILE = "input"


def split_columns(line, n):
	return [line[i:i+n] for i in range(0, len(line), n + 1)]


def build_stacks(stack_data):
	stack_data.reverse()
	stack_count = int(stack_data[0].split(' ')[-1])
	stacks = [[] for i in range(stack_count)]
	for line in stack_data[1:]:
		columns = split_columns(line, 3)
		for (i,item) in enumerate(columns):
			if item[1] != ' ':
				stacks[i].append(item[1])
	return stacks



def get_moves(move_data):
	moves = []
	for line in move_data:
		_, count, _, src, _, dest = line.split(' ')
		moves.append((int(count), int(src), int(dest)))
	return moves


def prepare_data(file_name):
	data = read_file(file_name)
	index_empty_line = data.index('')
	stack_data = data[:index_empty_line]
	move_data = data[index_empty_line+1:]
	stacks = build_stacks(stack_data)
	moves = get_moves(move_data)
	return stacks, moves


def move_items(stacks, moves):
	for move in moves:
		count, src, dest = move
		for _ in range(count):
			stacks[dest - 1].append(stacks[src - 1].pop())
	return stacks


def solve_part1(stacks, moves):
	stacks = move_items(stacks, moves)
	return ''.join([stack[-1] for stack in stacks])


print("part 1 (example):")
print(solve_part1(*prepare_data(EXAMPLE_FILE)))
print("part 1 (puzzle):")
print(solve_part1(*prepare_data(INPUT_FILE)))


def move_stacks(stacks, moves):
	for move in moves:
		# print(stacks, move)
		count, src, dest = move
		src = stacks[src - 1]
		dest = stacks[dest - 1]
		dest.extend(src[(len(src) - count):])
		del src[(len(src) - count):]
	return stacks


def solve_part2(stacks, moves):
	stacks = move_stacks(stacks, moves)
	return ''.join([stack[-1] for stack in stacks])


print("part 2 (example):")
print(solve_part2(*prepare_data(EXAMPLE_FILE)))
print("part 2 (puzzle):")
print(solve_part2(*prepare_data(INPUT_FILE)))
