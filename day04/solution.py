def parse_input(file_path):
    with open(file_path, "r") as file:
        data = [list(line.strip()) for line in file]
    return data


def solution1(data, pattern="XMAS"):
    def find_pattern(line, pattern):
        reversed_patten = "".join(list(reversed("XMAS")))
        return "".join(line).count(pattern) + "".join(line).count(reversed_patten)

    def get_diagonals(grid, bltr=True):
        dim = len(grid)
        assert dim == len(grid[0])
        return_grid = [[] for _ in range(2 * len(grid) - 1)]
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if bltr:
                    return_grid[row + col].append(grid[col][row])
                else:
                    return_grid[col - row + (dim - 1)].append(grid[row][col])
        return return_grid

    occurences = 0
    occurences += sum([find_pattern(l, pattern) for l in data])

    rotated = list(list(x) for x in zip(*data))[::-1]
    # top <-> bottom
    occurences += sum([find_pattern(l, pattern) for l in rotated])

    # bottom left to top right diagonals
    diag_bltr = get_diagonals(data)
    occurences += sum([find_pattern(l, pattern) for l in diag_bltr])

    # bottom right to top left diagonals
    diag_brtl = get_diagonals(data, bltr=False)
    occurences += sum([find_pattern(l, pattern) for l in diag_brtl])

    print("solution 1:", occurences)


def solution2(data):
    xmas = 0
    for r_idx, row in enumerate(data):
        for c_idx, col in enumerate(row):
            if (
                col == "A"
                and r_idx > 0
                and r_idx < len(row) - 1
                and c_idx > 0
                and c_idx < len(row) - 1
            ):
                # find diagonal occurences
                top_left = data[r_idx - 1][c_idx - 1]
                top_right = data[r_idx - 1][c_idx + 1]
                bottom_left = data[r_idx + 1][c_idx - 1]
                bottom_right = data[r_idx + 1][c_idx + 1]
                if (
                    (top_left == "M" and bottom_right == "S")
                    or (top_left == "S" and bottom_right == "M")
                ) and (
                    (top_right == "S" and bottom_left == "M")
                    or (top_right == "M" and bottom_left == "S")
                ):
                    xmas += 1
    print("solution 2", xmas)


data = parse_input("input.txt")
solution1(data)
solution2(data)
