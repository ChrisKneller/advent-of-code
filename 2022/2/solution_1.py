from functools import reduce as r


def solve():
    with open('input.txt', 'r') as f:

        # 148 characters
        return r((lambda x, y: x + {"A X": 4, "A Y": 8, "A Z": 3, "B X": 1, "B Y": 5, "B Z": 9, "C X": 7, "C Y": 2, "C Z": 6}[y]), f.read().splitlines(), 0)


if __name__ == "__main__":
    print(solve())
