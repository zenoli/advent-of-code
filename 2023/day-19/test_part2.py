import os
from part2 import (
    solve,
    generate_constraint_blocks,
    invert_condition,
    get_block,
    intersect,
    is_valid_block,
)


def test_invert_condition():
    assert invert_condition({"category": "a", "op": "<", "thresh": 2006}) == {
        "category": "a",
        "op": ">",
        "thresh": 2005,
    }
    assert invert_condition({"category": "a", "op": ">", "thresh": 2006}) == {
        "category": "a",
        "op": "<",
        "thresh": 2007,
    }


def test_get_block():
    condition = {"category": "a", "op": "<", "thresh": 2006}
    block = get_block(condition)
    for k, v in {
        "x": (1, 4001),
        "m": (1, 4001),
        "a": (1, 2006),
        "s": (1, 4001),
    }.items():
        assert block[k] == v

    block = get_block(invert_condition(condition))
    for k, v in {
        "x": (1, 4001),
        "m": (1, 4001),
        "a": (2006, 4001),
        "s": (1, 4001),
    }.items():
        assert block[k] == v


def test_intersect():
    c1 = {"category": "a", "op": "<", "thresh": 2006}
    c2 = {"category": "m", "op": ">", "thresh": 2090}
    c3 = {"category": "m", "op": "<", "thresh": 3000}

    b1 = get_block(c1)
    b2 = get_block(c2)
    b3 = get_block(c3)
    i1 = intersect(b1, b2)
    assert i1 == {
        "x": (1, 4001),
        "m": (2091, 4001),
        "a": (1, 2006),
        "s": (1, 4001),
    }
    i2 = intersect(i1, b3)

    assert i2 == {
        "x": (1, 4001),
        "m": (2091, 3000),
        "a": (1, 2006),
        "s": (1, 4001),
    }


def test_is_valid_block():
    assert is_valid_block(
        {
            "x": (1, 4001),
            "m": (2091, 4001),
            "a": (1, 2006),
            "s": (1, 4001),
        }
    )
    assert not is_valid_block(
        {
            "x": (1, 4001),
            "m": (2091, 4001),
            "a": (3000, 2006),
            "s": (1, 4001),
        }
    )


def test_generate_constraint_blocks():
    rules = [
        ({"category": "a", "op": "<", "thresh": 2006}, "qkq"),
        ({"category": "m", "op": ">", "thresh": 2090}, "A"),
        (None, "rfg"),
    ]
    constraint_blocks = generate_constraint_blocks(rules)
    assert constraint_blocks == [
        (
            {
                "x": (1, 4001),
                "m": (1, 4001),
                "a": (1, 2006),
                "s": (1, 4001),
            },
            "qkq",
        ),
        (
            {
                "x": (1, 4001),
                "m": (2091, 4001),
                "a": (2006, 4001),
                "s": (1, 4001),
            },
            "A",
        ),
        (
            {
                "x": (1, 4001),
                "m": (1, 2091),
                "a": (2006, 4001),
                "s": (1, 4001),
            },
            "rfg",
        ),
    ]


def test_part2():
    assert solve("day-19/sample.txt") == 167409079868000
