lines = open("input", "r").read()[:-1].split("\n")

# A, X => Rock
# B, Y => Paper
# C, Z => Siccors


def shape_score(shape):
    if shape == "A":
        return 1
    elif shape == "B":
        return 2
    elif shape == "C":
        return 3
    else:
        raise ValueError


def outcome_score(win):
    if win == 1:
        return 6
    elif win == 0:
        return 3
    elif win == -1:
        return 0


def is_winning(opponent, player):
    if opponent == player:
        return 0
    if opponent == "A" and player == "B":
        return 1
    elif opponent == "A" and player == "C":
        return -1
    elif opponent == "B" and player == "A":
        return -1
    elif opponent == "B" and player == "C":
        return 1
    elif opponent == "C" and player == "A":
        return 1
    elif opponent == "C" and player == "B":
        return -1


def translate_shape(player):
    if player == "X":
        return "A"
    elif player == "Y":
        return "B"
    elif player == "Z":
        return "C"


score = 0
for line in lines:
    score += shape_score(translate_shape(line[2])) + outcome_score(
        is_winning(line[0], translate_shape(line[2])))

print(score)


def translate_win(player):
    if player == "X":
        return -1
    elif player == "Y":
        return 0
    elif player == "Z":
        return 1


def get_move(opponent, should_win):
    for move in ["A", "B", "C"]:
        if is_winning(opponent, move) == should_win:
            return move


score = 0
for line in lines:
    should_win = translate_win(line[2])
    score += outcome_score(should_win) + \
        shape_score(get_move(line[0], should_win))

print(score)
