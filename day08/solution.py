import functools
import operator
import itertools


def parse_input(file_path):
    with open(file_path, "r") as file:
        data = [list(line.strip()) for line in file]
    return data


def solution1(data):
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
                antinodes.add((c1[0] - dist_x, c1[1] - dist_y))
                antinodes.add((c2[0] + dist_x, c2[1] + dist_y))
            if not c1_x and not c2_x:
                antinodes.add((c2[0] - dist_x, c2[1] - dist_y))
                antinodes.add((c1[0] + dist_x, c1[1] + dist_y))

            if c1_x and not c2_x:
                antinodes.add((c1[0] - dist_x, c1[1] + dist_y))
                antinodes.add((c2[0] + dist_x, c2[1] - dist_y))
            if (not c1_x) and c2_x:
                antinodes.add((c1[0] + dist_x, c1[1] - dist_y))
                antinodes.add((c2[0] - dist_x, c2[1] + dist_y))

    # remove antinodes outside of grid
    antinodes = {tup for tup in antinodes if all(0 <= x < len(data) for x in tup)}

    print("solution 1: ", len(antinodes))


data = parse_input("input.txt")
solution1(data)
