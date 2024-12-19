import time
import re
import copy

TEST_INPUT = False
if TEST_INPUT:
    filename = "testinput.txt"
else:
    filename = "input.txt"


def parse_input(file_path):
    with open(file_path, "r") as file:
        input = file.read()

        towels, displays = input.strip().split("\n\n")
        towels = towels.split(", ")
        displays = displays.split()
    return towels, displays


def word_construction_problem(towels, target):
    """
    Implements the word construction problem, calculating how many possible solutions
    there are to build the target string.
    Has an array (dp) to store integers, where dp[i] represents the number of
    ways the substring target[:i] can be formed using the given strings."""
    # initialise that every substring cannot be constructed
    dp = [0] * (len(target) + 1)
    dp[0] = 1  # Base case: empty string can be formed

    # go through the target string one by one
    for i in range(1, len(target) + 1):
        # check every given towel to build from
        for word in towels:
            # if the towel would fit into the substring and the last len(towel) characters
            # of the substring are equal to the towel
            # then set this part of the solution can be build (if the substring before towel can be build)
            if i >= len(word) and target[i - len(word) : i] == word:
                # on spot i, there are now + many solutions as in the
                # array before the word began
                dp[i] += dp[i - len(word)]

    return dp[-1]


def solution1(towels, displays):

    possible_combinations = 0
    for display in displays:
        possible = word_construction_problem(towels, display)
        possible_combinations += int(possible > 0)
    return possible_combinations


def solution2(towels, displays):

    possible_combinations = 0
    for display in displays:
        possible = word_construction_problem(towels, display)
        possible_combinations += int(possible)
    return possible_combinations


towels, displays = parse_input(filename)

start_time = time.time()
sol1 = solution1(towels, displays)
print(f"solution 1: {sol1} (runtime: {(time.time() - start_time)} seconds)")

start_time = time.time()
sol2 = solution2(towels, displays)
print(f"solution 2: {sol2} (runtime: {(time.time() - start_time)} seconds)")
