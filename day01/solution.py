from collections import Counter


def parse_input(file_path):
    with open(file_path, "r") as file:
        data = [list(map(int, line.strip().split("   "))) for line in file]
    return [d[0] for d in data], [d[1] for d in data]


def distance(lines1, lines2):
    lines1, lines2 = sorted(lines1), sorted(lines2)
    dist = sum(abs(a - b) for a, b in zip(lines1, lines2))
    print(dist)


def similarity(lines1, lines2):
    cnt = Counter(
        lines2
    )  # count occurences, runtime O(n), better than list.count(elem)
    sim = sum([x * cnt.get(x, 0) for x in lines1])
    print(sim)


l1, l2 = parse_input("testinput.txt")
distance(l1, l2)
similarity(l1, l2)
