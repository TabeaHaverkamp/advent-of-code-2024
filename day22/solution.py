import time
from collections import defaultdict


TEST_INPUT = False
if TEST_INPUT:
    filename = "testinput.txt"
    generate_numbers = 2000
else:
    filename = "input.txt"
    generate_numbers = 2000


my_pattern = (-2, 1, -1, 3)
# my_pattern = (-1, -1, 0, 2)


def parse_input(file_path):
    with open(file_path, "r") as file:
        data = list(map(int, [line.strip() for line in file]))
    return data


def secret_number(secret_number):
    number1 = ((secret_number * 64) ^ secret_number) % 16777216
    number2 = (int(number1 / 32) ^ number1) % 16777216
    number3 = (number2 * 2048) ^ number2
    number = number3 % 16777216
    return number


def solution1(data):
    secret_sum = 0
    for s in data:
        for _ in range(generate_numbers):
            s = secret_number(s)
        secret_sum += s
    return secret_sum


def find_first_occurrence(lst, cost_list, pattern):
    pattern_length = len(pattern)
    for i in range(len(lst) - pattern_length + 1):
        if tuple(lst[i : i + pattern_length]) == pattern:
            return cost_list[i + pattern_length - 1]  # return costs of first occurence
    return None


def find_repeating_patterns_optimized(pattern_lists, cost_lists, pattern_length=4):
    pattern_counts = defaultdict(int)
    pattern_costs = []
    all_seen_patterns = set()

    # Process each list
    for cost_lst, pattern_lst in zip(cost_lists, pattern_lists):
        seen_patterns = {}
        pattern_cst = defaultdict(int)
        # Use a sliding window to extract patterns
        for i in range(len(pattern_lst) - pattern_length + 1):
            pattern = tuple(pattern_lst[i : i + pattern_length])
            if pattern not in seen_patterns:
                # First occurrence of this pattern in the current list
                seen_patterns[pattern] = i
                pattern_counts[pattern] += 1

        # Add the seen patterns for this list to the global set
        all_seen_patterns.update(seen_patterns.keys())

        # Map patterns to their first costs directly
        for pattern, first_index in seen_patterns.items():
            pattern_cst[pattern] = cost_lst[first_index]

        # Append costs for this list
        pattern_costs.append(pattern_cst)

    return pattern_costs


def solution2(data):
    # get the costs and patterns through all the instructions
    costs = []
    patterns = []
    for s in data:
        price = s % 10
        c = []
        p = []
        for _ in range(generate_numbers):
            s = secret_number(s)
            new_price = s % 10

            p.append(new_price - price)
            c.append(new_price)
            price = new_price
        costs.append(c)
        patterns.append(p)
    # get all patterns that exist
    pattern_cost = find_repeating_patterns_optimized(
        cost_lists=costs, pattern_lists=patterns
    )

    result = defaultdict(int)
    for lst in pattern_cost:
        for key, value in lst.items():
            result[key] = result[key] + value

    return max(result.values())


data = parse_input(filename)


start_time = time.time()
sol1 = solution1(data)
print(f"solution 1: {sol1} (runtime: {(time.time() - start_time)} seconds)")


start_time = time.time()
sol2 = solution2(data)
print(f"solution 2: {sol2} (runtime: {(time.time() - start_time)} seconds)")
