from itertools import accumulate as a

def solve():
    with open('input.txt', 'r') as f:

        # 86 characters
        return max(a(f.read().splitlines(), (lambda x, y: x + int(y) if y else 0), initial=0))

if __name__ == "__main__":
    print(solve())