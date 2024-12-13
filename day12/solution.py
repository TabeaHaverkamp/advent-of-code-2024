import time


def parse_input(file_path):
    with open(file_path, "r") as file:
        data = [list(line.strip()) for line in file]
    return data


def solution1(data):
    def expand_area(data, index, direction, visited=set(), fence_count=0):
        i, j = index
        n_i = i + direction[0]
        n_j = j + direction[1]
        new_index = (n_i, n_j)
        visited.add(index)
        # print(f"checking {new_index} (old: {index}) against {data[i][j]}... {visited}")
        if new_index in visited:
            return visited, fence_count
        elif any(map(lambda x: x < 0, new_index)) or any(
            map(lambda x: x >= len(data), new_index)
        ):
            # print(f"  2  out of bounds {new_index}, {fence_count+1}")
            return visited, fence_count + 1
        elif data[i][j] == data[n_i][n_j]:
            visited.add(new_index)
            v = set()
            f = 0
            # print(f"  adding{new_index}...")
            for k in directions.values():
                kv, kf = expand_area(data, new_index, k, visited)
                v = v | kv
                f += kf
            return v, f
        else:
            # print(
            #     f"  1  {data[i][j]} != {data[n_i][n_j]}, {visited}, {fence_count + 1}"
            # )
            return visited, fence_count + 1

    all_visited = set()
    all_fence_cost = 0
    for r_idx, row in enumerate(data):
        for c_idx, _ in enumerate(row):
            v = set()
            i = (r_idx, c_idx)
            if i not in all_visited:
                uv, uf = expand_area(data, i, directions["U"], v)
                dv, df = expand_area(data, i, directions["D"], v)
                lv, lf = expand_area(data, i, directions["L"], v)
                rv, rf = expand_area(data, i, directions["R"], v)

                v = uv | dv | lv | rv
                f = sum([uf, df, lf, rf])
                all_visited = all_visited | v
                # print(
                #     f"checking index {i}, value: {elem}. elems in group: {len(v)},{v} fences needed: {f}. cost for {elem}: {len(v)*f}"
                # )
                all_fence_cost += len(v) * f

    return all_fence_cost


def solution2(data):
    def combine_dicts(list_of_dicts):
        combined_dict = {}
        for d in list_of_dicts:
            for key, value in d.items():
                combined_dict.setdefault(key, set()).update(value)

        return combined_dict

    def expand_area(data, index, d, visited=set(), borders={}):
        i, j = index
        direction = directions[d]
        n_i = i + direction[0]
        n_j = j + direction[1]
        new_index = (n_i, n_j)
        visited.add(index)
        # print(f"checking {new_index} (old: {index}) against {data[i][j]}... {visited}")
        if new_index in visited:
            return visited, borders
        elif any(map(lambda x: x < 0, new_index)) or any(
            map(lambda x: x >= len(data), new_index)
        ):
            # print(f"  2  out of bounds {index}, {borders}")
            borders.setdefault(d, []).append(index)
            return visited, borders
        elif data[i][j] == data[n_i][n_j]:
            visited.add(new_index)
            v = set()
            f = {}
            # print(f"  adding{new_index}...")

            for k in directions.keys():
                kv, kf = expand_area(data, new_index, k, visited, borders)
                v = v | kv
                f = combine_dicts([f, kf])
            return v, f
        else:
            # print(f"  1  {data[i][j]} != {data[n_i][n_j]}, {index}, {borders}")
            borders.setdefault(d, []).append(index)
            return visited, borders

    all_visited = set()
    all_fence_cost = 0
    for r_idx, row in enumerate(data):
        for c_idx, elem in enumerate(row):
            i = (r_idx, c_idx)
            if i not in all_visited:
                v = set()
                combine_dict = {}
                for k in directions.keys():
                    kv, kf = expand_area(data, i, k, set(), {})
                    v = v | kv
                    combine_dict = combine_dicts([combine_dict, kf])

                sides = 0
                for direction, borders in combine_dict.items():
                    borders = sorted(list(borders))
                    move = directions[border_check_dir[direction]]
                    side_counter = 0
                    for border_elem in borders:
                        next_border_elem = tuple(
                            map(lambda x, y: x + y, border_elem, move)
                        )
                        if next_border_elem not in borders:
                            side_counter += 1
                    sides += side_counter

                all_visited = all_visited | v

                all_fence_cost += len(v) * sides

    return all_fence_cost


directions = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

data = parse_input("input.txt")


start_time = time.time()
sol1 = solution1(data)
print(f"solution 1: {sol1} (runtime: {(time.time() - start_time)} seconds)")


border_check_dir = {"U": "R", "D": "R", "R": "D", "L": "D"}

start_time = time.time()
sol2 = solution2(data)
print(f"solution 2: {sol2} (runtime: {(time.time() - start_time)} seconds)")
