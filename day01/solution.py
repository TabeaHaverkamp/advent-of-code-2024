
def parse_input(file_path):
    with open(file_path, 'r') as file:
        data = [list(map(int, line.strip().split("   "))) for line in file]
    return [d[0] for d in data], [d[1] for d in data]

def distance(lines1, lines2):
    lines1, lines2 = sorted(lines1), sorted(lines2)
    dist = sum(abs(a - b) for a, b in zip(lines1, lines2))
    print(dist)


def similarity(lines1, lines2):
    sim = sum(x * lines2.count(x) for x in lines1)
    print(sim)
lines1, lines2 = parse_input('testinput.txt')
distance(lines1, lines2)      
similarity(lines1, lines2)