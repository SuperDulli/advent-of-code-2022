# %%
def read_file(file_name):
	with open(file_name, "r") as f:
		data = f.read().splitlines()
	return data

# %%
EXAMPLE_FILE = "example"
INPUT_FILE = "input"
# head won't move diagonally
head_directions = {'U':(0,1), 'D':(0,-1), 'R':(1,0), 'L':(-1,0)}

# %%
def prepare_data(file_name):
	moves = []
	data = read_file(file_name)
	for line in data:
		direction, count = line.split(' ')
		moves.append((head_directions[direction], int(count)))
	return moves
prepare_data(EXAMPLE_FILE)


# %%
# moves = prepare_data(EXAMPLE_FILE)
moves = prepare_data(INPUT_FILE)

# %%
def create_map(width, height, start_x, start_y):
	matrix = []
	for _ in range(height):
		matrix.append([' ' for _ in range(width)])
	matrix[start_y][start_x] = 'S'
	return matrix

pos_map = create_map(5,5, 2,2)
path_map = create_map(5,5, 2,2)

# %%
def print_map(m):
	for line in m:
		print(line)
	print()

# %%
def get_map_extremas(moves):
	x, y = 0, 0
	x_pos, y_pos = [], []
	for m in moves:
		x += m[0][0] * m[1]
		y += m[0][1] * m[1]
		x_pos.append(x)
		y_pos.append(y)
	return((min(x_pos), max(x_pos),min(y_pos), max(y_pos)))

print(get_map_extremas(prepare_data(EXAMPLE_FILE)))
get_map_extremas(prepare_data(INPUT_FILE))

# %%
def generate_maps(moves):
	x_min, x_max, y_min, y_max = get_map_extremas(moves)
	# print(x_min, x_max, y_min, y_max)
	width = abs(x_max - x_min) + 1
	height = abs(y_max - y_min) + 1
	pos_map = create_map(width, height, abs(x_min), abs(y_min))
	path_map = create_map(width, height, abs(x_min), abs(y_min))
	return (pos_map, path_map, (abs(x_min), abs(y_min)))

# %%
def move_head(pos_map, x, y, direction):
	if pos_map[y][x] == 'H':
		pos_map[y][x] = ' '
	pos_map[y + direction[1]][x + direction[0]] = 'H'
	return (x + direction[0], y + direction[1])

move_head(pos_map, 0,0,(0,1))
pos_map

# %%
def vector(start, end):
	return (end[0] - start[0], end[1] - start[1])

vector((5,5),(3,4))

# %%
def get_direction_from_vector(vector):
	result = [0,0]
	if vector[0] < 0:
		result[0] = -1
	elif vector[0] > 0:
		result[0] = 1
	if vector[1] < 0:
		result[1] = -1
	elif vector[1] > 0:
		result[1] = 1
	return tuple(result)

get_direction_from_vector((5,-1))

# %%
def is_touching(tail_pos, head_pos):
	if tail_pos[0] == head_pos[0] and abs(tail_pos[1] - head_pos[1]) <= 1:
		return True
	elif tail_pos[1] == head_pos[1] and abs(tail_pos[0] - head_pos[0]) <= 1:
		return True
	elif abs(tail_pos[0]- head_pos[0]) <= 1 and abs(tail_pos[1] - head_pos[1]) <= 1:
		return True
	return False

is_touching((5,5),(7,5))

# %%
def update_tail(pos_map, path_map, tail_pos, head_pos):
	if is_touching(tail_pos, head_pos):
		return tail_pos
	vec = get_direction_from_vector(vector(tail_pos, head_pos))
	if pos_map[tail_pos[1]][tail_pos[0]] == 'T':
		pos_map[tail_pos[1]][tail_pos[0]] = ' '
	pos_map[tail_pos[1] + vec[1]][tail_pos[0] + vec[0]] = 'T'
	path_map[tail_pos[1] + vec[1]][tail_pos[0] + vec[0]] = '#'
	return (tail_pos[0] + vec[0], tail_pos[1] + vec[1])


# %%
def simulate(moves):
	pos_map,path_map, start_pos = generate_maps(moves)
	head_pos = start_pos
	tail_pos = start_pos
	print(head_pos, tail_pos)
	for m in moves:
		print(m)
		for _ in range(m[1]):
			head_pos = move_head(pos_map, *head_pos, m[0])
			# print_map(pos_map)
			tail_pos = update_tail(pos_map, path_map, tail_pos, head_pos)
	return path_map

visited = simulate(moves)

# %%
def count_visited(path_map):
	count = 0
	for line in path_map:
		for tile in line:
			if tile != ' ':
				count += 1
	return count

count_visited(visited)


