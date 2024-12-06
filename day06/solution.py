import copy


def parse_input(file_path):
    with open(file_path, "r") as file:
        data = [list(line.strip()) for line in file]
        # Target symbols
        symbols = {"v": "D", "<": "L", ">": "R", "^": "U"}

        # Find the first occurrence
        index = next(
            (
                (i, j)
                for i, row in enumerate(data)
                for j, element in enumerate(row)
                if element in symbols.keys()
            ),
            None,
        )

    return (data, index, symbols[data[index[0]][index[1]]])


def solution1(data, index, direction):

    directions = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
    turns = {"U": "R", "R": "D", "D": "L", "L": "U"}
    counter = 0
    out = False
    while not out:
        add = directions[direction]
        new_index = (index[0] + add[0], index[1] + add[1])

        if (
            new_index[0] > len(data) - 1
            or new_index[1] > len(data[0]) - 1
            or new_index[0] < 0
            or new_index[1] < 0
        ):
            out = True
            s = data[index[0]][index[1]]
        else:
            s = data[new_index[0]][new_index[1]]

        if s == "." or s == "X":
            data[index[0]][index[1]] = "X"
            index = new_index
            if s == ".":
                counter += 1
        elif s == "#":
            direction = turns[direction]
    return data, counter


def solution2(data, index, direction):
    def check_loop(data, index, direction):
        directions = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
        turns = {"U": "R", "R": "D", "D": "L", "L": "U"}
        visited = set()
        while True:
            add = directions[direction]
            new_index = (index[0] + add[0], index[1] + add[1])
            if (
                new_index[0] > len(data) - 1
                or new_index[1] > len(data[0]) - 1
                or new_index[0] < 0
                or new_index[1] < 0
            ):
                return 0
            else:
                s = data[new_index[0]][new_index[1]]

            if (new_index, direction) in visited:
                return 1
            elif s == "." or s in directions.keys():
                if data[index[0]][index[1]] not in directions.keys():
                    data[index[0]][index[1]] = direction
                index = new_index
                visited.add((index, direction))

            elif s == "#" or s == "O" or s in directions.keys():
                data[index[0]][index[1]] = direction
                direction = turns[direction]

    walked, _ = solution1(copy.deepcopy(data), index, direction)
    loop_counter = 0
    for i, row in enumerate(walked):
        for j, elem in enumerate(row):
            if (i, j) != index and elem == "X":
                dat = copy.deepcopy(data)
                dat[i][j] = "O"
                cl = check_loop(dat, index, direction)
                loop_counter += cl
    return loop_counter


data, idx, direction = parse_input("input.txt")
print("solution 1: ", solution1(copy.deepcopy(data), idx, direction)[1])
print("solution 2: ", solution2(copy.deepcopy(data), idx, direction))
