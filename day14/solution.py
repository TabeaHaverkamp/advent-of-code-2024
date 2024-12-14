from functools import reduce
import time
import re


def parse_input(file_path):
    with open(file_path, "r") as file:
        input = file.read()
        result = []

        for batch in input.strip().split("\n"):
            px, py, vx, vy = map(int, re.findall("(-?\d+)", batch))

            result.append([(px, py), (vx, vy)])
    return result


def solution1(data, test_input=False):
    if test_input:
        size = (7, 11)  # might need to remove 1 here to start from 0
    else:
        size = (103, 101)
    result = {}
    for robot in data:
        # print(robot[0], robot[1])
        pos_y, pos_x = robot[0]
        vel_y, vel_x = robot[1]
        for _ in range(100):
            pos_x = (pos_x + vel_x) % size[0]
            pos_y = (pos_y + vel_y) % size[1]

        result[(pos_x, pos_y)] = result.get((pos_x, pos_y), 0) + 1
        res = [["." for _ in range(size[1])] for _ in range(size[0])]
        for k, v in result.items():
            res[k[0]][k[1]] = str(v)

    res = [[0 for _ in range(size[1])] for _ in range(size[0])]
    for k, v in result.items():
        res[k[0]][k[1]] = v

    # get the quadrants:
    mid_col, mid_row = size[0] // 2, size[1] // 2
    q1 = [row[:mid_row] for row in res[:mid_col]]
    q2 = [row[:mid_row] for row in res[mid_col + 1 :]]
    q3 = [row[mid_row + 1 :] for row in res[:mid_col]]
    q4 = [row[mid_row + 1 :] for row in res[mid_col + 1 :]]

    quadrant_sum = reduce(
        lambda x, y: x * y,
        [sum(sum(row) for row in matrix) for matrix in [q1, q2, q3, q4]],
    )
    return quadrant_sum


def solution2(data, test_input=False, print_tree=False):

    if test_input:
        size = (7, 11)
    else:
        size = (103, 101)
    found_christmas_tree = False
    i = 1
    while not found_christmas_tree:
        result = {}

        res = [["." for _ in range(size[1])] for _ in range(size[0])]
        for idx, robot in enumerate(data):

            pos_y, pos_x = robot[0]
            vel_y, vel_x = robot[1]
            pos_x = (pos_x + vel_x) % size[0]
            pos_y = (pos_y + vel_y) % size[1]

            result[(pos_x, pos_y)] = result.get((pos_x, pos_y), 0) + 1

            data[idx] = [(pos_y, pos_x), robot[1]]

        # build the display
        for k in result.keys():
            res[k[0]][k[1]] = "X"

        pattern = "XXXXXXXXXXXXXXXXX"

        if sum(pattern in "".join(s) for s in res) >= 3:
            if print_tree:
                print("-------", i, "-----")
                for l in res:
                    print("".join(l), pattern in "".join(l))
            found_christmas_tree = True
        if i >= 10000:
            print("end of loop!")
            found_christmas_tree = True
        i += 1

    return i - 1


data = parse_input("input.txt")

start_time = time.time()
sol1 = solution1(data, test_input=False)
print(f"solution 1: {sol1} (runtime: {(time.time() - start_time)} seconds)")


start_time = time.time()
sol2 = solution2(data, test_input=False, print_tree=False)
print(f"solution 2: {sol2} (runtime: {(time.time() - start_time)} seconds)")
