from functools import lru_cache


@lru_cache
def solve(n):
    if n <= 1:
        return n
    else:
        return solve(n - 1) + solve(n - 2)


if __name__ == "__main__":
    n = int(input())
    print(solve(n))
