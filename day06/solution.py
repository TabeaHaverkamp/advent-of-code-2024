import copy
import time


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
        direction = symbols[data[index[0]][index[1]]]
        data[index[0]][index[1]] = "."

    return (data, index, direction)


def solution1(data, index, direction):
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
            visited.add(index)
            return visited
        else:
            s = data[new_index[0]][new_index[1]]
            if s == ".":
                visited.add(index)
                index = new_index
            elif s == "#":
                direction = turns[direction]


def solution2(data, index, direction):
    def check_loop(data, index, direction, made_obstacle):

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

            if (index, direction) in visited:
                return 1
            elif s == "#" or new_index == made_obstacle:
                direction = turns[direction]
            elif s == ".":
                visited.add((index, direction))
                index = new_index

    walked = solution1(data, index, direction)
    loop_counter = 0
    for i, row in enumerate(data):
        for j, _ in enumerate(row):
            if (i, j) != index and (i, j) in walked:
                loop_counter += check_loop(data, index, direction, (i, j))
    return loop_counter


directions = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
turns = {"U": "R", "R": "D", "D": "L", "L": "U"}

start_time = time.time()

data, idx, direction = parse_input("input.txt")
print("solution 1: ", len(solution1(data, idx, direction)))
print("solution 2: ", solution2(data, idx, direction))
print("--- %s seconds ---" % (time.time() - start_time))
