import numpy as np


BELOW = np.array([1, 0])
ABOVE = np.array([-1, 0])
LEFT = np.array([0, -1])
RIGHT = np.array([0, 1])


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


def move(current_pos, prev_pos, pipe):
    direction = prev_pos - current_pos
    next_direction = pipes[pipe][all(pipes[pipe][0] == direction)]
    next_pos = current_pos + next_direction
    return next_pos


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
    lines = read_input("input.txt")
    pipe_map = np.array(list(map(list, lines)))
    start_pos = np.argwhere(pipe_map == "S")[0]

    prev_pos = start_pos
    current_pos = get_first_position(start_pos, pipe_map)
    dist = 1

    while not np.array_equal(current_pos, start_pos):
        next_pos = move(current_pos, prev_pos, pipe_map[tuple(current_pos)])
        prev_pos = current_pos
        current_pos = next_pos
        dist += 1

    print(dist // 2)


if __name__ == "__main__":
    main()
