# Special Fibonacci


def special_fib(a, b, n):
    if n % 3 == 0:
        return a
    elif n % 3 == 1:
        return b
    else:
        return a ^ b

# Read input
T = int(input("Enter number of test cases: "))
results = []

for _ in range(T):
    a, b, n = map(int, input().split())
    results.append(special_fib(a, b, n))

# Print results
for result in results:
    print(result)
