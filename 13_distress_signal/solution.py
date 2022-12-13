from functools import cmp_to_key


def read_file(file_name):
    with open(file_name, "r") as f:
        data = f.read().splitlines()
    return data


EXAMPLE_FILE = "example"
INPUT_FILE = "input"
# special divider packets
divider_packets = [[[2]], [[6]]]


def prepare_data(file_name):
    pairs = []
    pair = []
    for line in read_file(file_name):
        if line == "":
            pairs.append(pair[:])
            pair = []
            continue
        pair.append(eval(line))
    pairs.append(pair[:])
    return pairs


example_pairs = prepare_data(EXAMPLE_FILE)
pairs = prepare_data(INPUT_FILE)


def in_correct_order(lhs, rhs):
    if type(lhs) == int and type(rhs) == int:
        return lhs - rhs
    elif type(lhs) == list and type(rhs) == list:
        for i in range(max(len(lhs), len(rhs))):
            if i not in range(len(lhs)):
                return -1
            elif i not in range(len(rhs)):
                return 1
            a = lhs[i]
            b = rhs[i]
            result = in_correct_order(a, b)
            if result != 0:
                return result
        return 0
    elif type(lhs) == int:
        return in_correct_order([lhs], rhs)
    else:
        return in_correct_order(lhs, [rhs])

    return False


def solve_part(pairs):
    index = 1
    index_sum = 0
    for pair in pairs:
        if in_correct_order(pair[0], pair[1]) <= 0:
            index_sum += index
        index += 1
    return index_sum


print("## Part 1 ##")
print(solve_part(example_pairs))
print(solve_part(pairs))


def get_packets(file_name):
    packets = divider_packets[:]
    for line in read_file(file_name):
        if line != "":
            packets.append(eval(line))
    return packets


example_packets = get_packets(EXAMPLE_FILE)
packets = get_packets(INPUT_FILE)


def solve_part2(packets):
    result = 1
    packets.sort(key=cmp_to_key(in_correct_order))
    for d in divider_packets:
        result *= packets.index(d) + 1
    return result


print("## Part 1 ##")
print(solve_part2(example_packets))
print(solve_part2(packets))
