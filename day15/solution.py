import time
import re


def parse_input(file_path, solution_part=1):
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

        if solution_part == 2:
            w = []
            for l in warehouse:
                s = ""
                for elem in l:
                    if elem == ".":
                        s += ".."
                    elif elem == "#":
                        s += "##"
                    elif elem == "O":
                        s += "[]"
                    elif elem == "@":
                        s += "@."
                w.append(list(s))
            index = next(
                (
                    (i, j)
                    for i, row in enumerate(w)
                    for j, element in enumerate(row)
                    if element == "@"
                ),
                None,
            )
            return w, instructions, index
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


def solution2(warehouse, instructions, index):

    def move_up_down(warehouse, index, direction, moving={}):
        if moving == -1:
            return -1
        new_index = move(index, directions[direction])

        if new_index in moving.keys():
            return moving
        new_elem = warehouse[new_index[0]][new_index[1]]
        if new_elem in "[]":
            if new_elem == "[":
                moving[new_index] = moving.get(new_index, "[")
                other = (new_index[0], new_index[1] + 1)
                moving[other] = moving.get(other, "]")

            elif new_elem == "]":
                moving[new_index] = moving.get(new_index, "]")
                other = (new_index[0], new_index[1] - 1)
                moving[other] = moving.get(other, "[")
            # print("found indexes", new_index, other, direction)
            moving_1 = move_up_down(warehouse, new_index, direction, moving)
            moving_2 = move_up_down(warehouse, other, direction, moving)
            if moving_1 == -1 or moving_2 == -1:
                return -1
            moving.update(moving_1)
            moving.update(moving_2)

            return moving
        elif new_elem == "#":
            return -1
        else:
            return moving

    # move according to instructions
    for i, direction in enumerate(instructions):
        new_index = move(index, directions[direction])

        new_elem = warehouse[new_index[0]][new_index[1]]
        if new_elem == ".":  # can just move:
            warehouse[index[0]][index[1]] = "."
            warehouse[new_index[0]][new_index[1]] = "@"
            index = new_index

        elif new_elem in "[]":  # moooove
            moving = move_up_down(warehouse, index, direction, {})
            replace = False
            if moving != -1:  # when not reached border during move

                replace = True
                for k, v in moving.items():
                    moved_index = move(k, directions[direction])
                    if warehouse[moved_index[0]][moved_index[1]] == "#":
                        replace = False

            if replace:
                # clean slate for moving: remove all old brackets
                for k, v in moving.items():
                    warehouse[k[0]][k[1]] = "."
                # write new brackets:
                for k, v in moving.items():
                    moved_index = move(k, directions[direction])
                    warehouse[moved_index[0]][moved_index[1]] = v

                warehouse[new_index[0]][new_index[1]] = "@"
                warehouse[index[0]][index[1]] = "."

                index = new_index

    # get the GPS value
    object_indexes = [
        (i, j)
        for i, row in enumerate(warehouse)
        for j, elem in enumerate(row)
        if elem == "["
    ]
    gps = sum((100 * x) + y for x, y in object_indexes)
    return gps


directions = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}

warehouse, instructions, position = parse_input("input.txt")
start_time = time.time()
sol1 = solution1(warehouse, instructions, position)
print(f"solution 1: {sol1} (runtime: {(time.time() - start_time)} seconds)")

warehouse, instructions, position = parse_input("input.txt", solution_part=2)
start_time = time.time()
sol2 = solution2(warehouse, instructions, position)
print(f"solution 2: {sol2} (runtime: {(time.time() - start_time)} seconds)")
