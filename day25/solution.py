import time
from itertools import product

TEST_INPUT = False
if TEST_INPUT:
    filename = "testinput.txt"
else:
    filename = "input.txt"


def print_debug(data):
    max_length = max(len(str(cell)) for row in data for cell in row)
    for l in data:
        print(" ".join(f"{cell:<{max_length}}" for cell in l))


def parse_input(file_path):
    with open(file_path, "r") as file:
        input = file.read()
        keys = []
        locks = []

        blocks = input.split("\n\n")
        for block in blocks:
            block = [line for line in block.split("\n")]
            if "." in block[0]:
                keys.append(block)
            else:
                locks.append(block)
        return keys, locks


def solution1(keys, locks):
    def get_heights_keys(data):
        return [line.count("#") - 1 for line in list(list(x) for x in zip(*data))[::1]]

    def get_heights_locks(data):
        return [row.count("#") - 1 for row in [list(row) for row in zip(*data)][::1]]

    max_height = len(keys[0]) - 2

    correct_matches = 0
    for k, l in product(
        [get_heights_keys(k) for k in keys], [get_heights_locks(l) for l in locks]
    ):
        if all(x + y <= max_height for x, y in zip(l, k)):
            correct_matches += 1

    return correct_matches


keys, locks = parse_input(filename)


start_time = time.time()
sol1 = solution1(keys, locks)
print(f"solution 1: {sol1} (runtime: {(time.time() - start_time)} seconds)")
