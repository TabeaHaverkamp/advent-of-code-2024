import time
import re
import copy

TEST_INPUT = False
if TEST_INPUT:
    size = (7, 7)
    filename = "testinput.txt"
else:
    size = (71, 71)
    filename = "input.txt"
directions = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
turns = "UDRL"


def parse_input(file_path, solution_part=1, cutoff=1):
    with open(file_path, "r") as file:

        obstacles = [tuple(map(int, line.strip().split(","))) for line in file]
        if solution_part == 1:
            if TEST_INPUT:
                obstacles = obstacles[:12]
            else:
                obstacles = obstacles[:1024]
        elif solution_part == 2:
            obstacles = obstacles[:cutoff]
        matrix = [
            [float("inf") if (c, r) not in obstacles else "#" for c in range(size[0])]
            for r in range(size[1])
        ]
    return obstacles, matrix


def move(index, difference):
    """returns new index"""
    return tuple(map(lambda x, y: x + y, index, difference))


def print_debug(data):
    max_length = max(len(str(cell)) for row in data for cell in row)
    print(" ".join(f"{idx:<{max_length}}" for idx in range(len(data[0]))))
    for idx, l in enumerate(data):
        print(str(idx) + " ".join(f"{cell:<{max_length}}" for cell in l))


def solution1(data, debug=False):
    def dijkstra(data, current_index, current_direction):
        import heapq

        visit_dict = {
            (i, j): float("inf")
            for i, row in enumerate(data)
            for j, elem in enumerate(row)
            if elem != "#"
        }

        visit_dict[(current_index[0], current_index[1])] = 0
        to_visit = [(0, current_index, current_direction)]

        while len(to_visit) > 0:

            current_costs, current_index, current_direction = heapq.heappop(to_visit)
            # Skip if a shorter distance to current_node is already found
            if current_costs > visit_dict[(current_index[0], current_index[1])]:
                continue

            # Explore neighbors and update distances if a shorter path is found
            next_steps = []
            for turn in turns:
                next_index = move(current_index, directions[turn])
                weight = 1
                # if the next index is a valid element, append the possibility
                if next_index in visit_dict.keys():
                    next_steps.append((next_index, weight, turn))

            for neighbor, weight, turn in next_steps:
                cost = current_costs + weight
                # If shorter path to neighbor is found, update distance and push to queue
                if cost < visit_dict[neighbor]:
                    visit_dict[neighbor] = cost
                    heapq.heappush(to_visit, (cost, neighbor, turn))

        return visit_dict

    distance_map = dijkstra(data, (0, 0), "R")
    if debug:
        t = copy.deepcopy(data)
        for (i, j), dist in distance_map.items():
            t[i][j] = dist
        print_debug(t)
    sol = distance_map[(size[0] - 1, size[1] - 1)]
    return sol


def solution2():
    cutoff = 1
    inner_loop = True
    while True:
        obstacles, data = parse_input(filename, solution_part=2, cutoff=cutoff)
        sol = solution1(data)
        if sol == float("inf"):
            return obstacles[-1]
        else:
            while inner_loop:
                # to not go through it completely, increase by 100 until it not works anymore.
                # then reset the counter to the last possible solution and increase the counter by 1
                obstacles, data = parse_input(filename, solution_part=2, cutoff=cutoff)
                sol = solution1(data)
                if sol == float("inf"):
                    cutoff -= 100
                    inner_loop = False
                else:
                    cutoff += 100
        cutoff += 1


obstacles, data = parse_input(filename)

start_time = time.time()
sol1 = solution1(data=data)
print(f"solution 1: {sol1} (runtime: {(time.time() - start_time)} seconds)")


start_time = time.time()
sol2 = solution2()
print(f"solution 2: {sol2} (runtime: {(time.time() - start_time)} seconds)")
