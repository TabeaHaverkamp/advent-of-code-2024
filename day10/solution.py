import time


def parse_input(file_path):
    with open(file_path, "r") as file:
        data = [list(map(int, line.strip())) for line in file]
    return data


def solution1(data):

    def move(data, index, direction, sol=None, visited=None):
        i, j = index
        if sol is None:
            sol = set()
        if visited is None:
            visited = set()

        new_index = (i + direction[0], j + direction[1])
        n_i, n_j = new_index
        if any(map(lambda x: x < 0, new_index)) or any(
            map(lambda x: x >= len(data), new_index)
        ):
            return sol
        elif (n_i, n_j) in visited:
            return sol
        elif data[i][j] + 1 == data[n_i][n_j] == 9:
            sol.add((n_i, n_j))
            visited.add((n_i, n_j))
            return sol
        elif data[i][j] + 1 == data[n_i][n_j]:
            visited.add((n_i, n_j))
            u = move(data, (n_i, n_j), directions["U"], sol, visited)
            d = move(data, (n_i, n_j), directions["D"], sol, visited)
            l = move(data, (n_i, n_j), directions["L"], sol, visited)
            r = move(data, (n_i, n_j), directions["R"], sol, visited)
            return u | d | l | r
        else:
            return sol

    trails = sum(
        [
            len(
                move(data, (i, j), directions["U"])
                | move(data, (i, j), directions["D"])
                | move(data, (i, j), directions["L"])
                | move(data, (i, j), directions["R"])
            )
            for i, j in trailheads
        ]
    )
    return trails


def solution2(data):

    def move(data, index, direction, sol=None):
        i, j = index
        if sol is None:
            sol = dict()

        new_index = (i + direction[0], j + direction[1])
        n_i, n_j = new_index
        if any(map(lambda x: x < 0, new_index)) or any(
            map(lambda x: x >= len(data), new_index)
        ):
            return sol

        elif data[i][j] + 1 == data[n_i][n_j] == 9:
            sol[(n_i, n_j)] = sol.get((n_i, n_j), 0) + 1

            return sol
        elif data[i][j] + 1 == data[n_i][n_j]:
            u = move(data, (n_i, n_j), directions["U"], sol)
            d = move(data, (n_i, n_j), directions["D"], sol)
            l = move(data, (n_i, n_j), directions["L"], sol)
            r = move(data, (n_i, n_j), directions["R"], sol)
            return u | d | l | r
        else:
            return sol

    trails = 0
    for i, j in trailheads:
        u = move(data, (i, j), directions["U"])
        d = move(data, (i, j), directions["D"])
        l = move(data, (i, j), directions["L"])
        r = move(data, (i, j), directions["R"])

        solutions = (
            sum(u.values()) + sum(d.values()) + sum(l.values()) + sum(r.values())
        )

        trails += solutions

    return trails


data = parse_input("input.txt")
directions = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
trailheads = [
    (i, j) for i, row in enumerate(data) for j, value in enumerate(row) if value == 0
]

start_time = time.time()
sol1 = solution1(data)
print(f"solution 1: {sol1} (runtime: {(time.time() - start_time)} seconds)")


start_time = time.time()
sol2 = solution2(data)
print(f"solution 2: {sol2} (runtime: {(time.time() - start_time)} seconds)")
