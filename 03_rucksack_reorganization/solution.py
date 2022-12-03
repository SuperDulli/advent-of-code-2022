backpacks = open("input", "r").read().splitlines()


def find_shared_item(backpack):
    first = set(backpack[:len(backpack)//2])
    second = set(backpack[len(backpack)//2:])
    return first.intersection(second).pop()


def get_priority(letter):
    if letter.islower():
        return ord(letter) - 96  # a -> z == 1 -> 26
    return ord(letter) - 38  # A -> Z == 27 -> 52


priority_sum = 0
for backpack in backpacks:
    item = find_shared_item(backpack)
    priority_sum += get_priority(item)

print(priority_sum)

# Part 2


def find_badge(group):
    group = [set(x) for x in group]
    return group[0].intersection(group[1], group[2]).pop()


group_size = 3
groups = [backpacks[i:i + group_size]
          for i in range(0, len(backpacks), group_size)]

badge_sum = 0
for group in groups:
    badge = find_badge(group)
    badge_sum += get_priority(badge)

print(badge_sum)
