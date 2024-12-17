import time
import re


def parse_input(file_path, solution_part=1):
    with open(file_path, "r") as file:
        input = file.read()

        reg, program = input.strip().split("\n\n")
        program = list(map(int, program.split(":")[1].split(",")))
        reg = list(map(int, re.findall("(\d+)", reg)))
        registers = {k: v for k, v in zip(["A", "B", "C"], reg)}
    return registers, program


def solution1(registers, program):
    def get_instruction(opcode):
        match opcode:
            case 0:
                instruction = "adv"
            case 1:
                instruction = "bxl"
            case 2:
                instruction = "bst"
            case 3:
                instruction = "jnz"
            case 4:
                instruction = "bxc"
            case 5:
                instruction = "out"
            case 6:
                instruction = "bdv"
            case 7:
                instruction = "cdv"
        return instruction

    def get_combo_operand(op, register):
        if 0 <= op <= 3:
            return op
        elif op == 4:
            return register["A"]
        elif op == 5:
            return register["B"]
        elif op == 6:
            return register["C"]
        elif op == 7:
            raise ValueError
        else:
            raise ValueError

    def calculate(program, register, instruction_pointer, out):

        opcode = program[instruction_pointer]
        value = program[instruction_pointer + 1]
        instruction = get_instruction(opcode)
        match instruction:
            case "adv":
                adv = int(register["A"] / 2 ** get_combo_operand(value, register))
                register["A"] = adv
                instruction_pointer += 2
            case "bxl":
                bxl = register["B"] ^ value
                register["B"] = bxl
                instruction_pointer += 2
            case "bst":
                bst = get_combo_operand(value, register) % 8
                register["B"] = bst
                instruction_pointer += 2
            case "jnz":
                if register["A"] != 0:
                    instruction_pointer = value
                else:
                    instruction_pointer += 2
            case "bxc":
                bxc = register["B"] ^ register["C"]
                register["B"] = bxc
                instruction_pointer += 2
                # TODO is this ignored?
            case "out":
                o = get_combo_operand(value, register) % 8
                out.append(o)
                instruction_pointer += 2
            case "bdv":
                bdv = int(register["A"] / 2 ** get_combo_operand(value, register))
                register["B"] = bdv
                instruction_pointer += 2
            case "cdv":
                cdv = int(register["A"] / 2 ** get_combo_operand(value, register))
                register["C"] = cdv
                instruction_pointer += 2
        return register, instruction_pointer, out

    idx = 0
    out = []
    while idx < len(program):
        registers, idx, out = calculate(program, registers, idx, out)

    return ",".join(map(str, out))


registers, program = parse_input("input.txt")

start_time = time.time()
sol1 = solution1(registers, program)
print(f"solution 1: {sol1} (runtime: {(time.time() - start_time)} seconds)")
