import functools
import operator
import itertools
import time


def parse_input(file_path):
    with open(file_path, "r") as file:
        data = [list(line.strip()) for line in file]
    return data


def solution(data, solution_part=1):
    elems = set(functools.reduce(operator.iconcat, data, []))
    elems.remove(".")
    antinodes = set()
    for elem in elems:
        occ = [
            (ridx, cidx)
            for ridx, row in enumerate(data)
            for cidx, val in enumerate(row)
            if val == elem
        ]
        combinations = list(itertools.combinations(occ, 2))
        for c1, c2 in combinations:
            dist_x = abs(c1[0] - c2[0])
            dist_y = abs(c1[1] - c2[1])
            c1_x = c1[0] < c2[0]
            c2_x = c1[1] < c2[1]
            if c1_x and c2_x:
                if solution_part == 2:
                    i = 0
                    while c1[0] - i * dist_x >= 0 and c1[1] - i * dist_y >= 0:
                        antinodes.add((c1[0] - i * dist_x, c1[1] - i * dist_y))
                        i += 1
                    i = 0
                    while c2[0] + i * dist_x < len(data) and c2[1] + i * dist_y < len(
                        data
                    ):
                        antinodes.add((c2[0] + i * dist_x, c2[1] + i * dist_y))
                        i += 1
                elif solution_part == 1:
                    antinodes.add((c1[0] - dist_x, c1[1] - dist_y))
                    antinodes.add((c2[0] + dist_x, c2[1] + dist_y))

            if not c1_x and not c2_x:
                if solution_part == 2:
                    i = 0
                    while c2[0] - i * dist_x >= 0 and c2[1] - i * dist_y >= 0:
                        antinodes.add((c2[0] - i * dist_x, c2[1] - i * dist_y))
                        i += 1
                    i = 0
                    while c1[0] + i * dist_x < len(data) and c1[1] + i * dist_y < len(
                        data
                    ):
                        antinodes.add((c1[0] + i * dist_x, c1[1] + i * dist_y))
                        i += 1
                elif solution_part == 1:
                    antinodes.add((c2[0] - dist_x, c2[1] - dist_y))
                    antinodes.add((c1[0] + dist_x, c1[1] + dist_y))

            if c1_x and not c2_x:
                if solution_part == 2:
                    i = 0
                    while c1[0] - i * dist_x >= 0 and c1[1] + i * dist_y >= 0:
                        antinodes.add((c1[0] - i * dist_x, c1[1] + i * dist_y))
                        i += 1
                    i = 0
                    while c2[0] + i * dist_x < len(data) and c2[1] - i * dist_y < len(
                        data
                    ):
                        antinodes.add((c2[0] + i * dist_x, c2[1] - i * dist_y))
                        i += 1
                elif solution_part == 1:
                    antinodes.add((c1[0] - dist_x, c1[1] + dist_y))
                    antinodes.add((c2[0] + dist_x, c2[1] - dist_y))

            if (not c1_x) and c2_x:
                if solution_part == 2:
                    i = 0
                    while c1[0] + i * dist_x >= 0 and c1[1] - i * dist_y >= 0:
                        antinodes.add((c1[0] + i * dist_x, c1[1] - i * dist_y))
                        i += 1
                    i = 0
                    while c2[0] - i * dist_x < len(data) and c2[1] + i * dist_y < len(
                        data
                    ):
                        antinodes.add((c2[0] - i * dist_x, c2[1] + i * dist_y))
                        i += 1
                elif solution_part == 1:
                    antinodes.add((c1[0] + dist_x, c1[1] - dist_y))
                    antinodes.add((c2[0] - dist_x, c2[1] + dist_y))

    # remove antinodes outside of grid
    antinodes = {tup for tup in antinodes if all(0 <= x < len(data) for x in tup)}

    return len(antinodes)


data = parse_input("input.txt")
start_time = time.time()
sol1 = solution(data, solution_part=1)
print(f"solution 1: {sol1} (runtime: {(time.time() - start_time)} seconds)")

start_time = time.time()
sol2 = solution(data, solution_part=2)
print(f"solution 2: {sol2} (runtime: {(time.time() - start_time)} seconds)")
