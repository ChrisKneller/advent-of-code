from itertools import accumulate as a

def solve():
    with open('input.txt', 'r') as f:

        # 132 characters
        return -sum(sorted(list(a(f.read().splitlines(), (lambda x, y: -x if not y else int(y) if x < 0 else x + int(y)), initial=0)))[0:3])

if __name__ == "__main__":
    print(solve())
