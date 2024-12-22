import time
import copy
from itertools import product, permutations

TEST_INPUT = False
if TEST_INPUT:
    filename = "testinput.txt"
    generate_numbers = 2000
else:
    filename = "input.txt"
    generate_numbers = 2000


def parse_input(file_path):
    with open(file_path, "r") as file:
        data = map(int, [line.strip() for line in file])
    return data


def secret_number(secret_number):
    number1 = ((secret_number * 64) ^ secret_number) % 16777216
    number2 = (int(number1 / 32) ^ number1) % 16777216
    number3 = (number2 * 2048) ^ number2
    number = number3 % 16777216
    return number


def solution1(data):
    # bitwise XOR: ^
    secret_sum = 0
    for s in data:
        for _ in range(generate_numbers):
            s = secret_number(s)
        secret_sum += s
    return secret_sum


data = parse_input(filename)
print(data)
start_time = time.time()
sol1 = solution1(data)

print(f"solution 1: {sol1} (runtime: {(time.time() - start_time)} seconds)")
