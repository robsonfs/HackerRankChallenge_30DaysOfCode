def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

# Just to make the tests pass on HackerRank console.
if __name__ == '__main__':
    N = int(input())
    print(factorial(N))
