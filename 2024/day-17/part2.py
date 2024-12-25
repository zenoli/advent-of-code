from functools import cache


def read_input(filename: str):
    def parse_lines(lines: list[str]):
        def parse_register(line: str):
            return int(line.split(" ")[2])

        line_a, line_b, line_c, _, program = lines
        registers = map(parse_register, [line_a, line_b, line_c])
        program = map(int, program.split(" ")[1].split(","))
        return list(registers), list(program)

    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    return parse_lines(list(lines))


def main():
    @cache
    def run_program(A_in: int):
        out: list[str] = []

        A = A_in
        B = 0
        C = 0

        while True:
            # 2,4: bst(4)
            B = A % 8
            # 1,5: bxl(5)
            B = B ^ 0b101
            # 7,5: cdv(5)
            C = A // (1 << B)
            # 1,6: bxl(6)
            B = B ^ 0b110
            # 4,3: bxc()
            B = B ^ C
            # 5,5: out(5)
            out += str(B % 8)
            # 0,3: adv(3)
            A = A // 8
            # 3,0
            if A == 0:
                return out

    @cache
    def find_inputs(prg: str) -> set[str]:
        if len(prg) == 1:
            return {"3"}
        xs = prg[1:]
        inputs: set[str] = set()
        for i in range(8):
            inputs_xs = find_inputs(xs)
            for input_xs in inputs_xs:
                input_try = input_xs + str(i)
                output_try = "".join(run_program(to_dec(input_try)))
                if output_try == prg:
                    inputs.add(input_try)
        return inputs

    def dec(oct: int):
        return int(str(oct), 8)

    def to_dec(xs: str) -> int:
        return int(xs, 8)

    # registers, program = read_input("sample.txt")
    _, program = read_input("input.txt")

    program = "".join(map(str, program))

    inputs = find_inputs(program)
    result = dec(list(sorted(map(int, inputs)))[0])
    print(result)


if __name__ == "__main__":
    main()
