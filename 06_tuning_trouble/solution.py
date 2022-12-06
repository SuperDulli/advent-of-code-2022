def read_file(file_name):
    with open(file_name, "r") as f:
        data = f.read().splitlines()
    return data


INPUT_FILE = "input"
example0 = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"  # 7,19
example1 = "bvwbjplbgvbhsrlpgdmjqwftvncz"  # 5
example2 = "nppdvjthqldpwncqszvftbrmjlhg"  # 6, 23
example3 = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"  # 10, 29
example4 = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"  # 11, 26

examples = [example0, example1, example2, example3, example4]


def detect_marker(data, n):
    for count, _ in enumerate(data):
        if count < n:
            continue
        start_index = count - n
        window = data[start_index:count]
        if len(set(list(window))) == n:
            return count


def solve_part1(data):
    return detect_marker(data, 4)


print("## part 1 ##")

print("examples:")
for example in examples:
    print(solve_part1(example))

print("puzzle:", solve_part1(read_file(INPUT_FILE)[0]))


def solve_part2(data):
    return detect_marker(data, 14)


print("## part 2 ##")

print("examples:")
for example in examples:
    print(solve_part2(example))

print("puzzle:", solve_part2(read_file(INPUT_FILE)[0]))
