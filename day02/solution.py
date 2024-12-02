def parse_input(file_path):
    with open(file_path, "r") as file:
        data = [list(map(int, line.strip().split(" "))) for line in file]
    return data


def monotonically_increasing(l):
    return all(x < y and y - x <= 3 for x, y in zip(l, l[1:]))


def monotonically_decreasing(l):
    return monotonically_increasing(list(reversed(l)))


def problem1(data):

    print(
        "problem 1: ",
        sum(
            [
                1
                for i in data
                if monotonically_decreasing(i) or monotonically_increasing(i)
            ]
        ),
    )


def problem2(data):

    def nearly_monotonically_increasing(l):
        """Create a list of lists where one index is removed.
        Check those lists if it is now monotonically increasing.
        """
        comb = [
            [val for a_idx, val in enumerate(l) if a_idx != idx]
            for idx, _ in enumerate(l)
        ]

        return any(monotonically_increasing(c) for c in comb)

    def nearly_monotonically_decreasing(l):
        return nearly_monotonically_increasing(list(reversed(l)))

    print(
        "problem 2: ",
        sum(
            [
                sum(
                    [
                        nearly_monotonically_increasing(l),
                        nearly_monotonically_decreasing(l),
                    ]
                )
                for l in data
            ]
        ),
    )


data = parse_input("input.txt")
problem1(data)
problem2(data)
