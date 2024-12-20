import time
import copy
import heapq


TEST_INPUT = False
if TEST_INPUT:
    filename = "testinput.txt"
else:
    filename = "input.txt"

directions = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
turns = "UDRL"


def parse_input(file_path):
    with open(file_path, "r") as file:

        data = [list(line.strip()) for line in file]
        # Find the first occurrence
        start_index = next(
            (
                (i, j)
                for i, row in enumerate(data)
                for j, element in enumerate(row)
                if element == "S"
            ),
            None,
        )
        end_index = next(
            (
                (i, j)
                for i, row in enumerate(data)
                for j, element in enumerate(row)
                if element == "E"
            ),
            None,
        )
        data[start_index[0]][start_index[1]] = "."
        data[end_index[0]][end_index[1]] = "."
    return data, start_index, end_index


def move(index, difference):
    """returns new index"""
    return tuple(map(lambda x, y: x + y, index, difference))


def print_debug(data):
    max_length = max(len(str(cell)) for row in data for cell in row)
    print(" ".join(f"{idx:<{max_length}}" for idx in range(len(data[0]))))
    for idx, l in enumerate(data):
        print(str(idx) + " ".join(f"{cell:<{max_length}}" for cell in l))


def dijkstra(current_index, current_direction, border=None):

    visit_dict = {
        (i, j): float("inf")
        for i, row in enumerate(data)
        for j, elem in enumerate(row)
        if elem != "#"
    }

    if border:
        # add this border
        visit_dict[border] = float("inf")
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


def in_bounds(index, data_len):
    return not (
        any(map(lambda x: x < 0, index)) or any(map(lambda x: x >= data_len, index))
    )


def solution1(data, start):

    border_set = {
        (i, j)
        for i, row in enumerate(data)
        for j, elem in enumerate(row)
        if elem == "#"
    }

    def get_single_borders(border_set, bounds, distance_map):
        borders = set()
        for r, c in border_set:
            # Check neighbors
            updown = [(r - 1, c), (r + 1, c)]
            leftright = [(r, c - 1), (r, c + 1)]
            if all(neighbor not in border_set for neighbor in updown):
                if all(in_bounds(n, bounds) for n in updown):

                    dist_u = distance_map[move((r, c), directions["U"])]
                    dist_d = distance_map[move((r, c), directions["D"])]
                    if abs(dist_d - dist_u) > 100:
                        borders.add((r, c))

            elif all(neighbor not in border_set for neighbor in leftright):
                if all(in_bounds(n, bounds) for n in leftright):

                    dist_l = distance_map[move((r, c), directions["L"])]
                    dist_r = distance_map[move((r, c), directions["R"])]
                    if abs(dist_l - dist_r) > 100:
                        borders.add((r, c))

        return borders

    print(len(border_set))
    print(len(border_set))
    distance_map = dijkstra(start, "R")
    border_set = get_single_borders(border_set, len(data), distance_map)

    return len(border_set)


data, start_index, end_index = parse_input(filename)

start_time = time.time()
sol1 = solution1(data, start_index)
print(f"solution 1: {sol1} (runtime: {(time.time() - start_time)} seconds)")
