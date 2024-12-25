from functools import reduce


def read_input(filename):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    return lines[0].split(",")


def f(a, b):
    return (a + b) * 17 % 256

def hash(word):
    return reduce(f, map(ord, word), 0)

def main():
    # words = read_input("sample.txt")
    steps = read_input("input.txt")
    print(sum(map(hash, steps)))



if __name__ == "__main__":
    main()
