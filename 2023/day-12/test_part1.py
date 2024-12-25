from part1 import f, can_place


def test_can_place():
    assert not can_place("#", 3)
    assert not can_place("##", 1)
    assert can_place("#.", 1)
    assert can_place("#??.", 3)
    assert not can_place("#??.", 4)
    assert not can_place("#.?.", 3)


def test_f():
    assert f("???", (1, 1)) == 1
    assert f("???", (1,)) == 3
    assert f("?.?", (1,)) == 2
    assert f("###", (3,)) == 1
    assert f("?.###", (1, 3)) == 1
    assert f("##", (1,)) == 0
    assert f("?#?#?#?#?#?#?#?", (1, 3, 1, 6)) == 1
    assert f("##", (1,)) == 0
    assert f(".##", (3,)) == 0
    assert f("..???.??.?", (1, 1, 1)) == 9
    assert f(".....", (1, 1, 1)) == 0
    assert f("???????#?.#??", tuple()) == 0
