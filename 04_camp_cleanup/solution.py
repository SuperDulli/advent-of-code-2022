EXAMPLE_FILE = "example"
INPUT_FILE = "input"


def read_file(file_name):
    with open(file_name, "r") as f:
        data = f.read().splitlines()
    return data


exmaple_ranges = read_file(EXAMPLE_FILE)
ranges = read_file(INPUT_FILE)


def range_to_set(section):
    start, end = section.split('-')
    start = int(start)
    end = int(end) + 1
    return set(range(start, end))


def get_ranges(range_pair):
    left, right = range_pair.split(',')
    left = range_to_set(left)
    right = range_to_set(right)
    return (left, right)


def is_fully_contained(left, right):
    return left.issubset(right) or right.issubset(left)


def count_positves(sequence, test):
    count = 0
    for item in sequence:
        if test(*get_ranges(item)):
            count += 1
    return count


def solve_part1(ranges):
    return count_positves(ranges, is_fully_contained)


print(solve_part1(exmaple_ranges))
print(solve_part1(ranges))


def is_overlapping(left, right):
    return not left.isdisjoint(right)


def solve_part2(ranges):
    return count_positves(ranges, is_overlapping)


print(solve_part2(exmaple_ranges))
print(solve_part2(ranges))
