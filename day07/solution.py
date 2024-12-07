import time


def parse_input(file_path):
    with open(file_path, "r") as file:
        data = [
            (int(y[0]), list(map(int, y[1].split(" "))))
            for y in [line.strip().split(": ") for line in file]
        ]
    return data


def math(result, subtotal, input, solution_part):
    if len(input) == 0:
        return subtotal == result
    elif subtotal > result:
        return False

    i = input[0]
    if subtotal == 0:
        return math(result, i, input[1:], solution_part)

    plus = math(result, subtotal + i, input[1:], solution_part)
    if plus:
        return True
    mul = math(result, subtotal * i, input[1:], solution_part)
    if mul:
        return True

    if solution_part == 2:
        app = math(result, int(str(subtotal) + str(i)), input[1:], solution_part)
        if app:
            return True

    return False


def solution1(data):
    results = [math(result=l[0], subtotal=0, input=l[1], solution_part=1) for l in data]
    results = sum([i for (i, b) in zip([l[0] for l in data], results) if b])
    return results


def solution2(data):
    results = [math(result=l[0], subtotal=0, input=l[1], solution_part=2) for l in data]
    results = sum([i for (i, b) in zip([l[0] for l in data], results) if b])
    return results


data = parse_input("input.txt")
start_time = time.time()
sol1 = solution1(data)
print(f"solution 1: {sol1} (runtime: {(time.time() - start_time)} seconds)")

start_time = time.time()
sol2 = solution2(data)
print(f"solution 2: {sol2} (runtime: {(time.time() - start_time)} seconds)")
