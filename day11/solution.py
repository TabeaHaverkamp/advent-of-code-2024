import time


def parse_input(file_path):
    with open(file_path, "r") as file:
        data = [list(map(int, line.strip().split(" "))) for line in file][0]
    return data


def solution(data, r=25):
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
sol2 = solution(data, 75)
print(f"solution 2: {sol2} (runtime: {(time.time() - start_time)} seconds)")
