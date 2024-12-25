from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import StrEnum, auto
from collections import defaultdict
from typing import cast


class Op(StrEnum):
    XOR = auto()
    OR = auto()
    AND = auto()


@dataclass
class Evaluable(ABC):
    name: str

    @abstractmethod
    def eval(self) -> bool:
        pass


@dataclass
class Wire(Evaluable):
    state: bool

    def eval(self):
        return self.state

    def viz(self) -> str:
        return self.name


@dataclass
class Gate(Evaluable):
    wire1: Wire | Gate
    wire2: Wire | Gate

    op: Op

    def eval(self) -> bool:
        if self.op == Op.XOR:
            return self.wire1.eval() ^ self.wire2.eval()
        if self.op == Op.OR:
            return self.wire1.eval() | self.wire2.eval()
        else:
            return self.wire1.eval() & self.wire2.eval()

    def edges(self) -> list[tuple[str, str]]:
        res = [
            (self.name, self.wire1.name),
            (self.name, self.wire2.name),
        ]
        if isinstance(self.wire1, Gate):
            res = [*res, *self.wire1.edges()]
        if isinstance(self.wire2, Gate):
            res = [*res, *self.wire2.edges()]

        return res

    def to_graphviz_format(self):
        print("strict digraph {")
        for edge in self.edges():
            print(" -> ".join(edge))
        print("}")


def read_input(filename: str):
    inputs: dict[str, int] = {}
    gates: dict[str, tuple[str, str, str]] = {}
    with open(filename) as file:
        parse_inputs = True
        for line in file:
            line = line.rstrip()
            if line == "":
                parse_inputs = False
                continue

            if parse_inputs:
                splits = line.split(":")
                wire, state = splits[0], int(splits[1].strip())
                inputs[wire] = state
            else:
                wire1, op, wire2, _, out_wire = line.split()
                gates[out_wire] = (wire1, op, wire2)

    return inputs, gates


def to_number(outputs: list[bool]):
    return int("".join(str(int(b)) for b in outputs), 2)


def to_graphviz_format(graph):
    def vertex(v):
        return f'"{v}"'

    print("strict digraph {")
    for v, edges in graph.items():
        u1, u2, op = edges
        color: str
        if op == "XOR":
            color = "red"
        elif op == "AND":
            color = "blue"
        else:
            color = "yellow"
        # for u1 in edges:
        print(f'{vertex(v)} [color="{color}"]')
        print(f"{vertex(v)} -> {vertex(u1)}")
        print(f"{vertex(v)} -> {vertex(u2)}")
    print("}")


def to_graph(gates: dict[str, tuple[str, str, str]]):
    graph = defaultdict(list)
    for v, (wire1, op, wire2) in gates.items():
        graph[f"{v}"].extend([wire1, wire2, op])
    return graph


def main():
    def init(name: str):
        if name[0] in "xy":
            return Wire(name=name, state=bool(inputs[name]))
        wire1, op, wire2 = gates[name]
        return Gate(
            name=name,
            wire1=init(wire1),
            wire2=init(wire2),
            op=Op(op.lower()),
        )

    def verify_output_gate(gate: Evaluable):
        assert isinstance(gate, Gate)
        assert gate.name.startswith("z")
        if not gate.op == Op.XOR:
            yield gate.name

        assert isinstance(gate.wire1, Gate)
        assert isinstance(gate.wire2, Gate)

        if (
            gate.wire1.op == Op.XOR
            and gate.wire1.wire1.name[0] in "xy"
            and not gate.wire2.op == Op.OR
        ):
            yield gate.wire2.name
        if gate.wire1.op == Op.OR and not gate.wire2.op == Op.XOR:
            yield gate.wire2.name
        if (
            gate.wire2.op == Op.XOR
            and gate.wire2.wire1.name[0] in "xy"
            and not gate.wire1.op == Op.OR
        ):
            yield gate.wire1.name
        if gate.wire2.op == Op.OR and not gate.wire1.op == Op.XOR:
            yield gate.wire1.name

        yield from verify_last_carry_over_gate(
            gate.wire2 if gate.wire1.op == Op.XOR else gate.wire1
        )

    def verify_last_carry_over_gate(gate: Evaluable):
        assert isinstance(gate, Gate)
        assert isinstance(gate.wire1, Gate)
        assert isinstance(gate.wire2, Gate)
        if not gate.wire1.op == Op.AND:
            yield gate.wire1.name
        if not gate.wire2.op == Op.AND:
            yield gate.wire2.name

    # inputs, gates = read_input("sample.txt")
    inputs, gates = read_input("input.txt")

    # graph = to_graph(gates)
    # to_graphviz_format(graph)
    outputs = list(reversed(sorted(name for name in gates if name.startswith("z"))))
    out_gates = [cast(Gate, init(output)) for output in outputs]

    faulty_gates = []
    for out_gate in out_gates[1:-2]:
        try:
            for faulty_gate in verify_output_gate(out_gate):
                faulty_gates.append(faulty_gate)
        except AssertionError as e:
            continue

    print(",".join(sorted(faulty_gates)))


if __name__ == "__main__":
    main()
