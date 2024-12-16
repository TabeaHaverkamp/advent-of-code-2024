import time
import copy


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
    for l in data:
        print(" ".join(f"{cell:<{max_length}}" for cell in l))


def solution(data, start_index, end_index, solution_part=1, debug=False):

    def dijkstra(data, current_index, current_direction):
        import heapq

        visit_dict = {
            (i, j): float("inf")
            for i, row in enumerate(data)
            for j, elem in enumerate(row)
            if elem != "#"
        }

        visit_dict[(current_index[0], current_index[1])] = 0
        predecessors = {index: [] for index in visit_dict.keys()}
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
                next_neighbour = move(neighbor, directions[turn])
                # If shorter path to neighbor is found, update distance and push to queue
                if cost < visit_dict[neighbor]:
                    visit_dict[neighbor] = cost
                    predecessors[neighbor].append(current_index)
                    heapq.heappush(to_visit, (cost, neighbor, turn))
                elif cost == visit_dict[neighbor]:
                    predecessors[neighbor].append(current_index)
                elif (
                    next_neighbour in visit_dict.keys()
                    and cost <= visit_dict[next_neighbour]
                ):
                    predecessors[next_neighbour].append(current_index)

        return visit_dict, predecessors

    # Function to recursively collect all nodes in shortest paths
    def collect_shortest_paths(predecessors, index, visited):
        visited.add(index)
        if not predecessors[index]:
            return {index}
        for pred in predecessors[index]:
            visited.update(collect_shortest_paths(predecessors, pred, visited))
        return visited

    distance_map, predecessor = dijkstra(data, start_index, "R")

    if solution_part == 1:
        if debug:
            t = copy.deepcopy(data)
            for (i, j), dist in distance_map.items():
                t[i][j] = dist
            print_debug(t)
        sol = distance_map[end_index]
    elif solution_part == 2:
        visited_indexes = collect_shortest_paths(predecessor, end_index, set())
        if debug:
            t = copy.deepcopy(data)
            for i, j in visited_indexes:
                t[i][j] = "O"
            print_debug(t)
        sol = len(visited_indexes)
    else:
        sol = -1
    return sol


directions = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
turns = {"U": "URL", "R": "RDU", "D": "DLR", "L": "LUD"}

data, start_index, end_index = parse_input("input.txt")


start_time = time.time()
sol1 = solution(data, start_index, end_index, solution_part=1, debug=False)
print(f"solution 1: {sol1} (runtime: {(time.time() - start_time)} seconds)")


start_time = time.time()
sol2 = solution(data, start_index, end_index, solution_part=2, debug=False)
print(f"solution 2: {sol2} (runtime: {(time.time() - start_time)} seconds)")
