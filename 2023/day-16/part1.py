import numpy as np

Position = tuple[int, int]
Direction = Position

UP: Direction = (-1, 0)
DOWN: Direction = (1, 0)
LEFT: Direction = (0, -1)
RIGHT: Direction = (0, 1)


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def read_input(filename):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    return lines


def mirror_slash(x, y):
    return -y, -x


def mirror_backslash(x, y):
    return y, x


def debug(grid, seen):
    def formatter(x):
        if x == UP:
            return ""
        if x == DOWN:
            return ""
        if x == LEFT:
            return ""
        if x == RIGHT:
            return ""
        return " "

    for grid_row, seen_row in zip(grid, seen):
        print(
            " ".join(grid_row)
            + "  "
            + np.array2string(seen_row, formatter={"all": formatter})
        )
    print("=============================================")


def compute_next_positions(pos, direction, symbol):
    if symbol == "|" and direction in {LEFT, RIGHT}:
        return [(pos, UP), (pos, DOWN)]
    elif symbol == "-" and direction in {UP, DOWN}:
        return [(pos, LEFT), (pos, RIGHT)]
    elif symbol == "/":
        return [(pos, mirror_slash(*direction))]
    elif symbol == "\\":
        return [(pos, mirror_backslash(*direction))]
    else:
        return [(pos, direction)]


def cast_ray(pos, direction, grid):
    seen = np.full(grid.shape, None)

    N = len(grid)
    M = len(grid[0])

    beams: list[tuple[Position, Direction]] = [(pos, direction)]

    while beams:
        pos, direction = beams.pop()
        next_pos = add(pos, direction)

        if (
            next_pos[0] not in range(N)
            or next_pos[1] not in range(M)
            or seen[next_pos] == direction
        ):
            continue

        seen[next_pos] = direction
        beams.extend(compute_next_positions(next_pos, direction, grid[next_pos]))
        debug(grid, seen)

    return np.count_nonzero(seen)


def main():
    lines = read_input("sample.txt")
    # lines = read_input("input.txt")
    grid = np.array(list(map(list, lines)))

    energized_cells = cast_ray((0, -1), RIGHT, grid)
    print(energized_cells)


if __name__ == "__main__":
    main()
