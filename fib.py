from timeit import timeit
import fibbers
import sys

RUNS = 100


def fibonacci(n: int) -> int:
    return n if n <= 1 else fibonacci(n - 1) + fibonacci(n - 2)

def main():
    n = int(sys.argv[1])

    print(f"{fibonacci(n) = }")
    print(f"{fibbers.fib(n) = }")

    python_time_per_call = timeit(lambda: fibonacci(n), number=RUNS) / RUNS
    print(f"\n Python mms per call: {python_time_per_call * 1000000:.2f} mms")
    print(f"Python ms per call: {python_time_per_call * 1000:.2f} ms")

    rust_time_per_call = timeit(lambda: fibbers.fib(n), number=RUNS) / RUNS
    print(f"\n Rust mms per call: {rust_time_per_call * 1000000:.2f} mms")
    print(f"Rust ms per call: {rust_time_per_call * 1000:.2f} ms")

if __name__ == '__main__':
    main()
