import numpy as np
from itertools import pairwise
from skimage.morphology import flood


# Directions
BELOW = np.array([1, 0])
ABOVE = np.array([-1, 0])
LEFT = np.array([0, -1])
RIGHT = np.array([0, 1])

# Turns
RIGHT_TURN = 1
LEFT_TURN = -1
NEUTRAL = 0

pipes = {
    "L": (ABOVE, RIGHT),
    "7": (LEFT, BELOW),
    "F": (RIGHT, BELOW),
    "J": (ABOVE, LEFT),
    "|": (ABOVE, BELOW),
    "-": (LEFT, RIGHT),
}


def read_input(filename):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    return lines


def turn(direction, pipe):
    if pipe == "F":
        return RIGHT_TURN if np.array_equal(direction, BELOW) else LEFT_TURN
    if pipe == "7":
        return RIGHT_TURN if np.array_equal(direction, LEFT) else LEFT_TURN
    if pipe == "J":
        return RIGHT_TURN if np.array_equal(direction, ABOVE) else LEFT_TURN
    if pipe == "L":
        return RIGHT_TURN if np.array_equal(direction, RIGHT) else LEFT_TURN
    else:
        return NEUTRAL


def move(current_pos, prev_pos, pipe):
    direction = prev_pos - current_pos
    next_direction = pipes[pipe][all(pipes[pipe][0] == direction)]
    next_pos = current_pos + next_direction
    return next_pos, turn(direction, pipe)


def get_interior_neighbors(current_pos, prev_pos, orientation):
    direction = current_pos - prev_pos
    neightbor1 = current_pos + np.array([direction[1], -direction[0]]) * orientation
    neightbor2 = prev_pos + np.array([direction[1], -direction[0]]) * orientation
    return neightbor1, neightbor2


def get_first_position(start_pos, pipe_map):
    if pipe_map[tuple(start_pos + RIGHT)] in ["-", "J", "7"]:
        return start_pos + RIGHT
    if pipe_map[tuple(start_pos + LEFT)] in ["-", "F", "L"]:
        return start_pos + LEFT
    if pipe_map[tuple(start_pos + ABOVE)] in ["|", "F", "7"]:
        return start_pos + ABOVE
    else:
        return start_pos + BELOW


def main():
    # lines = read_input("sample1.txt")
    # lines = read_input("sample2.txt")
    # lines = read_input("sample3.txt")
    # lines = read_input("sample4.txt")
    lines = read_input("input.txt")
    pipe_map = np.array(list(map(list, lines)))
    start_pos = np.argwhere(pipe_map == "S")[0]

    prev_pos = start_pos
    current_pos = get_first_position(start_pos, pipe_map)
    dist = 1
    orientation = 0

    loop = [start_pos, current_pos]

    while not np.array_equal(current_pos, start_pos):
        next_pos, turn = move(current_pos, prev_pos, pipe_map[tuple(current_pos)])
        loop.append(next_pos)
        prev_pos = current_pos
        current_pos = next_pos
        dist += 1
        orientation += turn

    interior = np.full(pipe_map.shape, 0)
    interior_pretty = np.full(pipe_map.shape, " ")

    for step in loop:
        interior[tuple(step)] = 1

    if orientation > 0:
        orientation = 1
        print("RIGHT turning circle")
    else:
        orientation = -1
        print("LEFT turning circle")

    for prev_pos, current_pos in pairwise(loop):
        inner_neighbors = get_interior_neighbors(current_pos, prev_pos, orientation)
        for inner_neighbor in inner_neighbors:
            if interior[tuple(inner_neighbor)] == 0:
                mask = flood(interior, tuple(inner_neighbor))
                interior[mask] = 2

    interior_pretty[interior == 2] = "I"
    interior_pretty[interior == 1] = "x"

    print(interior_pretty)
    print(np.count_nonzero(interior == 2))

    np.savetxt("out/pipe-maze.txt", interior_pretty, fmt="%s", delimiter=" ")
    # print(np.array2string(interior, separator=", "))


if __name__ == "__main__":
    main()
