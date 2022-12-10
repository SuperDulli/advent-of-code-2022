def read_file(file_name):
	with open(file_name, "r") as f:
		data = f.read().splitlines()
	return data

EXAMPLE_FILE = "example"
INPUT_FILE = "input"
sample_cycles = [20]
for i in range(5):
	sample_cycles.append(sample_cycles[0] + 40 * (i + 1))

def prepare_data(file_name):
	instructions = []
	data = read_file(file_name)
	for line in data:
		if line == 'noop':
			instructions.append((line, 0, 1))
			continue
		operation, value = line.split(' ')
		instructions.append((operation, int(value), 2))
	return instructions

example_instructions = prepare_data(EXAMPLE_FILE)
instructions = prepare_data(INPUT_FILE)

def execute(instructions):
	signal_strength = 0 # part 1
	row = [] # part 2
	cycle = 1
	value = 1
	i = 0
	_, value_to_add, execution_time = instructions[i]
	while i < len(instructions) - 1:
		if cycle in sample_cycles:
			signal_strength += cycle * value
		if (cycle - 1) % 40 in range(value - 1, value +2):
			row.append('#')
		else:
			row.append(' ') # better readablity than '.'
		if cycle % 40 == 0:
			print(''.join(row))
			row = []
		execution_time -= 1
		if execution_time == 0:
			value += value_to_add
			i += 1
			_, value_to_add, execution_time = instructions[i]
		cycle += 1
	print(''.join(row))
	return signal_strength

print("## Example Input ##")
print(execute(example_instructions))
print("## Puzzle Input ##")
print(execute(instructions))
