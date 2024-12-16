import time
import re


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


def solution1(data, start_index, end_index, debug=False):

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

        while len(to_visit) > 0:  # and current_index != end_index:
            current_costs, current_index, current_direction = heapq.heappop(to_visit)

            # Skip if a shorter distance to current_node is already found
            if current_costs > visit_dict[(current_index[0], current_index[1])]:
                continue

            # Explore neighbors and update distances if a shorter path is found
            next_steps = []
            for turn in turns[current_direction]:
                next_index = move(current_index, directions[turn])
                if turn == current_direction:
                    weight = 1
                else:
                    weight = 1000 + 1
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

    distance_map = dijkstra(data, start_index, "R")
    if debug:
        for (i, j), dist in distance_map.items():
            data[i][j] = dist
        max_length = max(len(str(cell)) for row in data for cell in row)
        for l in data:
            print(" ".join(f"{cell:<{max_length}}" for cell in l))
    return distance_map[end_index]


directions = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
turns = {"U": "URL", "R": "RDU", "D": "DLR", "L": "LUD"}

data, start_index, end_index = parse_input("input.txt")


start_time = time.time()
sol1 = solution1(data, start_index, end_index)
print(f"solution 1: {sol1} (runtime: {(time.time() - start_time)} seconds)")
