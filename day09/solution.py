import time


def parse_input(file_path):
    with open(file_path, "r") as file:
        data = [list(line.strip()) for line in file]
    return data


def build_array(data):
    for line in data:
        block = ""
        f = []
        for idx, elem in enumerate(line):
            if idx % 2 == 0:
                block += "a" * int(elem)
                f.append([int(idx / 2)] * int(elem))
            else:
                block += "." * int(elem)
        f = [item for sublist in f for item in sublist]
    return block, f


def solution1(data):
    blocks, b = build_array(data)
    # print('blocks', blocks)
    # print('b', b)
    free_space = blocks.count(".")
    used_space = len(blocks) - free_space
    print(free_space, used_space)
    for idx, elem in enumerate(blocks):
        if idx > used_space:
            break
        if elem == ".":
            # print(b[:idx], b[-1], b[idx:])
            b.insert(idx, b[-1])
            b = b[:-1]
            # print(b[:idx])

    res = sum([idx * int(elem) for idx, elem in enumerate(b)])

    return res


data = parse_input("input.txt")
start_time = time.time()
sol1 = solution1(data)
print(f"solution 1: {sol1} (runtime: {(time.time() - start_time)} seconds)")

# start_time = time.time()
# sol1 = solution1(data)
# print(f"solution 2: {sol1} (runtime: {(time.time() - start_time)} seconds)")
