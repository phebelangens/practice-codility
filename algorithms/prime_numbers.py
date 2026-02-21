import time


class NthPrimeSolution:

    def solution(self, n: int) -> int:
        
        found_primes = []
        i = 2
        while len(found_primes) < n:
            if self.check_prime(i, found_primes):
                found_primes.append(i)
            i += 1
        return found_primes[-1]

    def check_prime(self, num: int, found_primes: list) -> bool:
        for prime in found_primes:
            if num % prime == 0:
                return False
        return True

if __name__ == "__main__":
    s = NthPrimeSolution()

    assert s.solution(1) == 2
    print("Test on n=1 returns 2")
    assert s.solution(4) == 7
    print("Test on n=4 returns 7")
    assert s.solution(6) == 13
    print("Test on n=6 returns 13")

    # n_large = 10_000
    # time_limit = 1.0

    # start = time.perf_counter()
    # result = s.solution(n_large)
    # elapsed = time.perf_counter() - start

    # assert elapsed < time_limit, f"Too slow: {elapsed:.4f}s (limit: {time_limit}s)"