import time
import networkx as nx
from collections import defaultdict

TEST_INPUT = False
if TEST_INPUT:
    filename = "testinput.txt"
else:
    filename = "input.txt"


def parse_input(file_path):
    with open(file_path, "r") as file:
        paths = [tuple(line.strip().split("-")) for line in file]
        G = nx.DiGraph(paths).to_undirected()

    return G


def solution1(graph):

    cycles = [
        cycle
        for cycle in nx.simple_cycles(graph, length_bound=3)
        if len(cycle) <= 3 and any(node.startswith("t") for node in cycle)
    ]

    return len(cycles)


def solution2(graph):

    cliques = list(nx.find_cliques(graph))
    biggest_clique = max(cliques, key=len)
    password = ",".join(sorted(biggest_clique))
    return password


graph = parse_input(filename)


start_time = time.time()
sol1 = solution1(graph)
print(f"solution 1: {sol1} (runtime: {(time.time() - start_time)} seconds)")


start_time = time.time()
sol2 = solution2(graph)
print(f"solution 2: {sol2} (runtime: {(time.time() - start_time)} seconds)")
