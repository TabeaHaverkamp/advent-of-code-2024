import time

import functools
import operator


def parse_input(file_path):
    with open(file_path, "r") as file:
        data = [list(line.strip()) for line in file]
    return data


def solution1(data):
    elems = list(set(i for j in data for i in j))
    print("set: ", elems)
    visited = []

    def add_group(g, key, value):
        a = g.get(key, set())
        a.add(value)
        return a

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
            # print(f"  adding{new_index}...")
            uv, uf = expand_area(data, new_index, directions["U"], visited)
            dv, df = expand_area(data, new_index, directions["D"], visited)
            lv, lf = expand_area(data, new_index, directions["L"], visited)
            rv, rf = expand_area(data, new_index, directions["R"], visited)

            visited = uv | dv | lv | rv
            return visited, sum([uf, df, lf, rf])
        else:
            # print(
            #     f"  1  {data[i][j]} != {data[n_i][n_j]}, {visited}, {fence_count + 1}"
            # )
            return visited, fence_count + 1

    # fences(data)
    all_visited = set()
    all_fence_cost = 0
    for r_idx, row in enumerate(data):
        for c_idx, elem in enumerate(row):
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
                print(
                    f"checking index {i}, value: {elem}. elems in group: {len(v)},{v} fences needed: {f}. cost for {elem}: {len(v)*f}"
                )
                all_fence_cost += len(v) * f

    return all_fence_cost


directions = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

data = parse_input("input.txt")


start_time = time.time()
sol1 = solution1(data)
print(f"solution 1: {sol1} (runtime: {(time.time() - start_time)} seconds)")
