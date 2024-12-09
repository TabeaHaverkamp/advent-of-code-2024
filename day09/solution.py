import time

import functools
import operator


def parse_input(file_path):
    with open(file_path, "r") as file:
        data = [list(line.strip()) for line in file]
    return data


def solution1(data):
    def build_array(data):
        data = data[0]
        block = ""
        f = []
        for idx, elem in enumerate(data):
            if idx % 2 == 0:
                block += "a" * int(elem)
                f.append([int(idx / 2)] * int(elem))
            else:
                block += "." * int(elem)
        f = [item for sublist in f for item in sublist]
        return block, f

    blocks, b = build_array(data)
    free_space = blocks.count(".")
    used_space = len(blocks) - free_space
    for idx, elem in enumerate(blocks):
        if idx > used_space:
            break
        if elem == ".":
            b.insert(idx, b[-1])
            b = b[:-1]
    res = sum([idx * int(elem) for idx, elem in enumerate(b)])

    return res


def solution2(data):
    def build_array(data):
        data = data[0]
        if len(data) % 2 != 0:
            data += "0"
        free = []
        used = []
        for idx, elem in enumerate(data):
            if idx % 2 == 0:
                used.append([int(idx / 2)] * int(elem))
            else:
                free.append(int(elem))
        return free, used

    free, used = build_array(data)
    b = [(a, ["."] * b, 0) for a, b in zip(used, free)]
    for ridx, elem in enumerate(list(reversed(used))):
        replaced = False
        free_idx = 0
        while (not replaced) and free_idx < len(free):
            j = len(used) - 1 - ridx  # to be removed, proper index of used
            if free_idx >= j or len(elem) == 0:
                replaced = True

            elif len(elem) <= b[free_idx][1].count("."):
                # insert into free spots at idx i
                u = b[free_idx][1]
                moved = b[free_idx][2]
                b[free_idx] = (
                    b[free_idx][0],
                    u[:moved] + elem + u[(len(elem) + moved) :],
                    moved + len(elem),
                )
                # remove from spot j
                b[j] = ([], ["."] * len(elem) + b[j][1], b[j][2])
                replaced = True

            free_idx += 1

    a = [item for sublist in [x + y for (x, y, _) in b] for item in sublist]
    res = sum([idx * elem for idx, elem in enumerate(a) if isinstance(elem, int)])

    return res


data = parse_input("input.txt")
start_time = time.time()
sol1 = solution1(data)
print(f"solution 1: {sol1} (runtime: {(time.time() - start_time)} seconds)")

start_time = time.time()
sol1 = solution2(data)
print(f"solution 2: {sol1} (runtime: {(time.time() - start_time)} seconds)")
