from sympy import symbols, Eq, solve
import time
import re


def parse_input(file_path):
    with open(file_path, "r") as file:
        input = file.read()
        result = []

        for batch in input.strip().split("\n\n"):
            ax, ay, bx, by, x, y = map(int, re.findall("(\d+)", batch))
            result.append([ax, ay, bx, by, x, y])
    return result


def solution(data, solution_part=1):
    button_costs = 0
    for _, prob in enumerate(data):
        a, b = symbols("a,b ")
        ax, ay, bx, by, x, y = prob
        if solution_part == 2:
            x += 10000000000000
            y += 10000000000000
        # defining equations
        eq1 = Eq((ax * a + bx * b), x)
        eq2 = Eq((ay * a + by * b), y)

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
