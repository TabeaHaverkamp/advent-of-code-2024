def parse_input(file_path):
    with open(file_path, "r") as file:
        data = [line.strip() for line in file]
        empty_line_index = data.index("")
        directions = {}
        for l in data[:empty_line_index]:
            k = l.split("|")[0]
            v = l.split("|")[1]
            directions.setdefault(k, []).append(v)
        checks = [l.split(",") for l in data[empty_line_index + 1 :]]

    return directions, checks


def solution1(directions, checks):
    correct_checks = 0
    for l in checks:
        correct = True
        for idx, val in enumerate(l):
            if val in directions.keys():
                direction_vals = [v for v in directions[val] if v in l]

                if (not all([dv in l[idx + 1 :] for dv in direction_vals])) and idx > 0:
                    correct = False
                    break
        if correct:
            correct_checks += int(l[int((len(l) - 1) / 2)])
    print(correct_checks)


directions, checks = parse_input("input.txt")
solution1(directions, checks)
