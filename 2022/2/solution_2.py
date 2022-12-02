from itertools import accumulate as a


def solve():
    with open('input.txt', 'r') as f:

        # 161 characters
        return max(a(f.read().splitlines(), (lambda x, y: x + {"A X": 3, "A Y": 4, "A Z": 8, "B X": 1, "B Y": 5, "B Z": 9, "C X": 2, "C Y": 6, "C Z": 7}[y]), initial=0))


if __name__ == "__main__":
    print(solve())
