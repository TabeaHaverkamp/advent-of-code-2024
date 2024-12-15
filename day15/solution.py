import time
import re


def parse_input(file_path):
    with open(file_path, "r") as file:
        input = file.read()
        warehouse, instructions = input.strip().split("\n\n")
        warehouse = [list(line) for line in warehouse.split("\n")]
        # Find the first occurrence
        index = next(
            (
                (i, j)
                for i, row in enumerate(warehouse)
                for j, element in enumerate(row)
                if element == "@"
            ),
            None,
        )
        instructions = [list(l) for l in ["".join(instructions.split("\n"))]][0]
    return warehouse, instructions, index


def move(index, difference):
    """returns new index"""
    return tuple(map(lambda x, y: x + y, index, difference))


def solution1(warehouse, instructions, index):

    # move according to instructions
    for i, direction in enumerate(instructions):
        new_index = move(index, directions[direction])

        if any(map(lambda x: x < 0, new_index)) or any(
            map(lambda x: x >= len(warehouse), new_index)
        ):
            print("out of bounds!")
            continue

        new_elem = warehouse[new_index[0]][new_index[1]]
        if new_elem == ".":  # can just move:
            warehouse[index[0]][index[1]] = "."
            warehouse[new_index[0]][new_index[1]] = "@"
            index = new_index

        elif new_elem == "O":  # moooove
            move_idx = new_index
            while warehouse[move_idx[0]][move_idx[1]] == "O":
                move_idx = move(move_idx, directions[direction])
            if warehouse[move_idx[0]][move_idx[1]] == ".":
                warehouse[move_idx[0]][move_idx[1]] = "O"
                warehouse[new_index[0]][new_index[1]] = "@"
                warehouse[index[0]][index[1]] = "."
                index = new_index
        # border doesnt need to be checked, because nothing is happening...

    # get the GPS value
    object_indexes = [
        (i, j)
        for i, row in enumerate(warehouse)
        for j, elem in enumerate(row)
        if elem == "O"
    ]
    gps = sum((100 * x) + y for x, y in object_indexes)
    return gps


directions = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}

warehouse, instructions, position = parse_input("input.txt")
start_time = time.time()
sol1 = solution1(warehouse, instructions, position)
print(f"solution 1: {sol1} (runtime: {(time.time() - start_time)} seconds)")
