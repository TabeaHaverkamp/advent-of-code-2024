import itertools
import time


def parse_input(file_path):
    with open(file_path, "r") as file:
        data = [list(line.strip()) for line in file]
    return data


def solution(data, solution_part=1):
    antennaes = {}
    for ridx, row in enumerate(data):
        for cidx, val in enumerate(row):
            if val != ".":
                antennaes.setdefault(val, []).append((ridx, cidx))

    antinodes = set()
    for _, occ in antennaes.items():
        combinations = list(itertools.product(occ, occ))
        for c1, c2 in combinations:
            if c1 == c2:
                continue
            dist_x = c1[0] - c2[0]
            dist_y = c1[1] - c2[1]

            if solution_part == 1:
                antinodes.add((c1[0] + dist_x, c1[1] + dist_y))
            elif solution_part == 2:
                i = 0
                while 0 <= c1[0] + i * dist_x < len(data) and 0 <= c1[
                    1
                ] + i * dist_y < len(data):
                    antinodes.add((c1[0] + i * dist_x, c1[1] + i * dist_y))
                    i += 1

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
