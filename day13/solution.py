from sympy import symbols, Eq, solve
import time


def parse_input(file_path):
    with open(file_path, "r") as file:
        input = file.read()
        result = []

        for batch in input.strip().split("\n\n"):
            lines = batch.splitlines()  # Split batch into individual lines
            batch_dict = {}
            for line in lines:
                key, value = line.split(":", 1)  # Split at the first colon
                if "=" in value:
                    split_char = "="
                else:
                    split_char = "+"
                value = [int(x.split(split_char)[1]) for x in value.strip().split(",")]

                batch_dict[key.strip()] = value
            result.append(batch_dict)
    return result


def solution(data, solution_part=1):
    button_costs = 0
    for _, prob in enumerate(data):
        a, b = symbols("a,b ")
        button_a = prob["Button A"]
        button_b = prob["Button B"]
        prize = prob["Prize"]
        if solution_part == 2:
            prize = [i + 10000000000000 for i in prize]
        # defining equations
        eq1 = Eq((button_a[0] * a + button_b[0] * b), prize[0])
        eq2 = Eq((button_a[1] * a + button_b[1] * b), prize[1])

        # solving the equation
        solutions = solve((eq1, eq2), (a, b))

        if solutions[a].is_integer and solutions[b].is_integer:
            button_cost = 3 * solutions[a] + solutions[b]
            button_costs += button_cost
    return button_costs


data = parse_input("input.txt")

start_time = time.time()
sol1 = solution(data, solution_part=1)
print(f"solution 1: {sol1} (runtime: {(time.time() - start_time)} seconds)")

start_time = time.time()
sol2 = solution(data, solution_part=2)
print(f"solution 2: {sol2} (runtime: {(time.time() - start_time)} seconds)")
