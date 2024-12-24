import time
from collections import defaultdict
import operator

TEST_INPUT = False
if TEST_INPUT:
    filename = "testinput.txt"
else:
    filename = "input.txt"


def parse_input(file_path):
    with open(file_path, "r") as file:
        input = file.read()

        start, gates = input.split("\n\n")
        start = [line for line in start.split("\n")]
        gates = [list(line) for line in gates.split("\n")]

        start = dict(["".join(l).split(": ") for l in start])
        start = {k: int(v) for k, v in start.items()}
        gates = ["".join(l).split(" -> ") for l in gates]

        operator_gates = defaultdict()
        ops = [" AND ", " XOR ", " OR "]
        for gate in gates:
            for o in ops:
                if o in gate[0]:
                    operator_gates[gate[1]] = tuple(
                        (sorted(gate[0].split(o)), o.strip())
                    )
    return start, operator_gates


def solution1(start_values, operator_gates):

    def op_replace_known_values(known_values, gates):
        for known_key, known_value in known_values.items():
            gates = {
                key: tuple(
                    (
                        [
                            known_value if value == known_key else value
                            for value in values[0]
                        ],
                        values[1],
                    )
                )
                for key, values in gates.items()
            }
        return gates

    def are_both_int(t):
        return (
            isinstance(t, list) and len(t) == 2 and all(isinstance(x, int) for x in t)
        )

    def calculate_new_solutions(known_values, gates):
        popped = []
        for key, value in gates.items():
            gate_type = value[1]
            gate_input = value[0]
            if are_both_int(gate_input):
                match gate_type:
                    case "AND":
                        known_values[key] = gate_input[0] & gate_input[1]
                    case "XOR":
                        known_values[key] = operator.xor(gate_input[0], gate_input[1])
                    case "OR":
                        known_values[key] = gate_input[0] | gate_input[1]
                popped.append(key)
        for key in popped:
            gates.pop(key)
        return known_values, gates

    def get_z_values(known_values):
        z_values = {
            key: value for key, value in known_values.items() if key.startswith("z")
        }
        binary_str = ""
        for _, v in reversed(sorted(z_values.items())):
            binary_str += str(v)
        return int(binary_str.lstrip("0"), 2)

    while any(s.startswith("z") for s in operator_gates.keys()):

        operator_gates = op_replace_known_values(start_values, operator_gates)
        start_values, operator_gates = calculate_new_solutions(
            start_values, operator_gates
        )

    return get_z_values(start_values)


start, operator_gates = parse_input(filename)


start_time = time.time()
sol1 = solution1(start, operator_gates)
print(f"solution 1: {sol1} (runtime: {(time.time() - start_time)} seconds)")
