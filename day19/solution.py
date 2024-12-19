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


def solution1(towels, displays):
    def word_construction(towels, target):
        """
        Implements the word construction problem.
        """
        # initialise that every substring cannot be constructed
        dp = [False] * (len(target) + 1)
        dp[0] = True  # Base case: empty string can be formed

        # go through the target string one by one
        for i in range(1, len(target) + 1):
            # check every given towel to build from
            for word in towels:
                # if the towel would fit into the substring and the last len(towel) characters
                # of the substring are equal to the towel
                # then set this part of the solution can be build (if the substring before towel can be build)
                if i >= len(word) and target[i - len(word) : i] == word:
                    dp[i] = dp[i] or dp[i - len(word)]

        return dp[-1]

    possible_combinations = 0
    for display in displays:
        possible = word_construction(towels, display)
        possible_combinations += int(possible)

    return possible_combinations


towels, displays = parse_input(filename)

start_time = time.time()
sol1 = solution1(towels, displays)
print(f"solution 1: {sol1} (runtime: {(time.time() - start_time)} seconds)")
