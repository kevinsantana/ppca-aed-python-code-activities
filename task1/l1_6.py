from math import sqrt


def divisors(n):
    large_divisors = []
    for i in range(1, int(sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i * i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield int(divisor)


if __name__ == "__main__":
    n = int(input())
    print(*list(divisors(n)), sep='\n')
