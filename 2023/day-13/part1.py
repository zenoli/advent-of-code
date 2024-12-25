from itertools import pairwise


def read_input(filename):
    patterns = []
    pattern = []
    with open(filename) as file:
        for line in file:
            line = line.rstrip()
            if not line:
                patterns.append(pattern)
                pattern = []
            else:
                pattern.append(line.rstrip())
    patterns.append(pattern)
    return patterns


def enc(pattern):
    def encode_line(line):
        enc = "1" + line.replace("#", "1").replace(".", "0")
        return int(enc, 2)

    return list(map(encode_line, pattern))


def find_palindrome(p):
    for i, (x, y) in enumerate(pairwise(p), 1):
        if x == y:
            seq1, seq2 = p[:i], p[i:]
            x = min(map(len, (seq1, seq2)))
            if seq1[::-1][:x] == seq2[:x]:
                return i


def transpose(pattern):
    def col(j):
        return "".join(pattern[i][j] for i in range(len(pattern)))

    return [col(j) for j in range(len(pattern[0]))]


def debug(pattern):
    for line in pattern:
        print(line)


def main():
    # patterns = read_input("sample.txt")
    patterns = read_input("input.txt")
    horizontal = sum(filter(None, (find_palindrome(enc(p)) for p in patterns)))
    vertical = sum(filter(None, (find_palindrome(enc(transpose(p))) for p in patterns)))

    result = 100 * horizontal + vertical
    print(result)


if __name__ == "__main__":
    main()
