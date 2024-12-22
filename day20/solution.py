import time
import copy
import heapq


TEST_INPUT = False
if TEST_INPUT:
    filename = "testinput.txt"
    cheat_len_part2 = 20
    cheat_len_part1 = 2

    saved_time = 76
else:
    filename = "input.txt"
    cheat_len_part2 = 20
    cheat_len_part1 = 2
    saved_time = 100

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


def dijkstra(data, current_index, current_direction, border=None):

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


def get_teleports(index, distance_map, cheat_len, saved_time):
    costs = 0
    for i in range(-cheat_len, cheat_len + 1):
        for j in range(-cheat_len, cheat_len + 1):
            if abs(i) + abs(j) <= cheat_len:
                new_index = move(index, (i, j))
                if new_index in distance_map:

                    if (
                        distance_map[index]
                        + abs(i)
                        + abs(j)  # new costs to get to new_index
                        <= distance_map[new_index] - saved_time
                    ):
                        costs += 1

    return costs


def solution1(data, start):

    distance_map = dijkstra(data, start, "R")

    found_cheats = 0
    for index in distance_map:
        found_cheats += get_teleports(index, distance_map, cheat_len_part1, saved_time)

    return found_cheats


def solution2(data, start):

    distance_map = dijkstra(data, start, "R")

    found_cheats = 0
    for index in distance_map:
        found_cheats += get_teleports(index, distance_map, cheat_len_part2, saved_time)

    return found_cheats


data, start_index, end_index = parse_input(filename)


start_time = time.time()
sol1 = solution1(data, start_index)
print(f"solution 1: {sol1} (runtime: {(time.time() - start_time)} seconds)")


start_time = time.time()
sol2 = solution2(data, start_index)
print(
    f"solution 2: {sol2} with min saved time {saved_time}, cheats: {cheat_len_part2} (runtime: {(time.time() - start_time)} seconds)"
)
