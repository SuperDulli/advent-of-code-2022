def read_file(file_name):
	with open(file_name, "r") as f:
		data = f.read().splitlines()
	return data

EXAMPLE_FILE = "example"
INPUT_FILE = "input"

def cab_distance(start, destination):
	return abs(start[0] - destination[0]) + abs(start[1] - destination[1])

def prepare_data(file_name):
	sensor_map = {}
	beacons = []
	data = read_file(file_name)
	for line in data:
		line = line.split(' ')
		sensor_x = int(line[2][2:-1])
		sensor_y = int(line[3][2:-1])
		beacon_x = int(line[8][2:-1])
		beacon_y = int(line[9][2:])
		distance = cab_distance((sensor_x, sensor_y), (beacon_x, beacon_y))
		sensor_map[(sensor_x, sensor_y)] = distance
		beacons.append((beacon_x, beacon_y))
	return (sensor_map, beacons)


def reachable_from_sensor(pos, sensor_map):
	for sensor_pos, distance in sensor_map.items():
		if cab_distance(sensor_pos, pos) <= distance:
			return True
	return False


def find_extremas(sensor_map):
	max_distance = max(sensor_map.values())
	x_coords = [x for x,y in sensor_map.keys()]
	return (min(x_coords) - max_distance, max(x_coords) + max_distance)


def solve_part1(file_name, row):
	count = 0
	sensor_map, beacons = prepare_data(file_name)
	min_x, max_x = find_extremas(sensor_map)
	for x in range(min_x, max_x + 1):
		if (x, row) in beacons:
			continue
		if reachable_from_sensor((x, row), sensor_map):
			count += 1
	return count

print("### Part 1 ###")
print(f"Example: {solve_part1(EXAMPLE_FILE, 10)}")
print(f"Puzzle: {solve_part1(INPUT_FILE, 2_000_000)}")

def tuning_frequency(x, y):
	return x * 4_000_000 + y

def neumann_neighbourhood_border(pos, distance):
	result = []
	x, y = pos
	for step in range(distance + 1):
		result.append((x + step, y - distance - 1 + step))
		result.append((x - step, y + distance + 1 - step))
		result.append((x - distance - 1 + step, y - step))
		result.append((x + distance + 1 - step, y + step))
	return result


def solve_part2(file_name, max_coord):
	sensor_map, beacons = prepare_data(file_name)
	checked = set()
	for sensor_pos, distance in sensor_map.items():
		for pos in neumann_neighbourhood_border(sensor_pos, distance):
			x, y = pos
			if x not in range(max_coord + 1) or y not in range(max_coord + 1) or pos in checked or pos in beacons:
				continue
			# TODO: remove sensor that create the hood
			if not reachable_from_sensor(pos, sensor_map):
				print(pos)
				return tuning_frequency(*pos)
		checked.add(pos)
	print("No solution found")
	return None

print("### Part 2 ###")
print(f"Example: {solve_part2(EXAMPLE_FILE, 20)}")
print(f"Puzzle: {solve_part2(INPUT_FILE, 4_000_000)}")
