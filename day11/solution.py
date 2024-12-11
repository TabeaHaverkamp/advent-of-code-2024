import time


def parse_input(file_path):
    with open(file_path, "r") as file:
        data = [list(map(int, line.strip().split(" "))) for line in file][0]
    return data


def solution(data, r=25):
    for _ in range(r):
        idx = 0
        l = len(data)
        while idx < l:
            elem = data[idx]
            if elem == 0:
                data[idx] = 1
                idx += 1
            elif len(str(elem)) % 2 == 0:
                s_e = str(elem)
                first = int(s_e[: int(len(s_e) / 2)])
                second = int(s_e[int(len(s_e) / 2) :])
                data[idx] = first
                data.append(second)
                idx += 1
            else:
                data[idx] = elem * 2024
                idx += 1

    return len(data)


def solution2(data, r=25):
    m = {d: 1 for d in data}
    for _ in range(r):
        a = {}

        for k, how_often in list(m.items()):
            if k == 0:
                a[1] = a.get(1, 0) + how_often
                m[k] = 0
            elif len(str(k)) % 2 == 0:
                s_e = str(k)
                first = int(s_e[: int(len(s_e) / 2)])
                second = int(s_e[int(len(s_e) / 2) :])

                a[first] = a.get(first, 0) + how_often
                a[second] = a.get(second, 0) + how_often

                m[k] = 0
            else:
                a[k * 2024] = a.get(k * 2024, 0) + how_often
                m[k] = 0
        m = a

    return sum(m.values())


data = parse_input("input.txt")
# testinput : 55.312
# input: 213.625
start_time = time.time()
sol1 = solution(data, 25)
print(f"solution 1: {sol1} (runtime: {(time.time() - start_time)} seconds)")


start_time = time.time()
sol2 = solution2(data, 75)
print(f"solution 2: {sol2} (runtime: {(time.time() - start_time)} seconds)")
