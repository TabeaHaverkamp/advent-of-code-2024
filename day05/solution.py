from functools import cmp_to_key


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
        d = {k: [val for val in v if val in l] for k, v in directions.items() if k in l}
        for idx, val in enumerate(l):
            if val in d.keys():

                if (not all([dv in l[idx + 1 :] for dv in d[val]])) and idx > 0:
                    correct = False
                    break
        if correct:
            correct_checks += int(l[int((len(l) - 1) / 2)])
    print("solution 1: ", correct_checks)


def solution2(directions, checks):

    def compare(item1, item2):
        if item1 in d.keys() and item2 in d[item1]:
            return -1
        elif item2 in d.keys() and item1 in d[item2]:
            return 1
        else:
            return 0

    correct_checks = 0

    for l in checks:
        d = {k: [val for val in v if val in l] for k, v in directions.items() if k in l}
        for idx, val in enumerate(l):
            if val in d.keys():
                if (not all([dv in l[idx + 1 :] for dv in d[val]])) and idx > 0:
                    sort = sorted(l, key=cmp_to_key(compare))
                    correct_checks += int(sort[int((len(sort) - 1) / 2)])
                    break

    print("solution 2: ", correct_checks)


directions, checks = parse_input("input.txt")
solution1(directions, checks)
solution2(directions, checks)
