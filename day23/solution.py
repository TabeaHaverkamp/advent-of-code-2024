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
    return paths


def solution1(edges):

    G = nx.DiGraph(edges).to_undirected()

    cycles = [
        cycle
        for cycle in nx.simple_cycles(G, length_bound=3)
        if any("t" == node[0] for node in cycle)
    ]

    return len(cycles)


def solution2(edges):

    G = nx.DiGraph(edges).to_undirected()
    cliques = list(nx.find_cliques(G))
    biggest_clique = max(cliques, key=len)
    password = ",".join(sorted(biggest_clique))
    return password


paths = parse_input(filename)


start_time = time.time()
sol1 = solution1(paths)
print(f"solution 1: {sol1} (runtime: {(time.time() - start_time)} seconds)")


start_time = time.time()
sol2 = solution2(paths)
print(f"solution 2: {sol2} (runtime: {(time.time() - start_time)} seconds)")
