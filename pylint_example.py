"""Simple utility module: primes and fibonacci demo."""

from typing import List

def is_prime(number: int) -> bool:
    """Return True if number is prime."""
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0:
        return False
    candidate = 3
    while candidate * candidate <= number:
        if number % candidate == 0:
            return False
        candidate += 2
    return True

def primes_upto(limit_value: int) -> List[int]:
    """Return primes up to limit_value (inclusive)."""
    primes = []
    for num in range(2, limit_value + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def fibonacci(count: int) -> List[int]:
    """Generate first count Fibonacci numbers."""
    if count <= 0:
        return []
    seq = [0, 1]
    while len(seq) < count:
        seq.append(seq[-1] + seq[-2])
    return seq[:count]

def main() -> None:
    """Run a short demo to print results."""
    print("Primes up to 30:")
    print(primes_upto(30))
    print("First 10 Fibonacci numbers:")
    print(fibonacci(10))

if __name__ == "__main__":
    main()

