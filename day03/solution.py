import re


def solution1(file_path):
    def parse_input(file_path):
        with open(file_path, "r") as file:
            data = [line.strip() for line in file]
            match_mul = "mul\(([0-9]{0,3}),([0-9]{0,3})\)"
            match = [re.findall(match_mul, l) for l in data]
            flat_matches = [(int(a), int(b)) for xs in match for (a, b) in xs]
        return flat_matches

    data = parse_input(file_path)
    print("solution 1: ", sum([i * j for (i, j) in data]))


def solution2(file_path):
    def parse_input(file_path):
        with open(file_path, "r") as file:
            data = "do()" + "-".join([line.strip() for line in file]) + "don't()"
            match_mul = "mul\(([0-9]{0,3}),([0-9]{0,3})\)"
            match_dos = "(?<=do\(\)).*?(?=don't\(\))"
            match = [re.findall(match_mul, l) for l in re.findall(match_dos, data)]
            flat_matches = [(int(a), int(b)) for xs in match for (a, b) in xs]
        return flat_matches

    data = parse_input(file_path)
    print("solution 2: ", sum([i * j for (i, j) in data]))


solution1("input.txt")
solution2("input.txt")
