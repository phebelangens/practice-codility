import time


class Fibonacci:

    def solution(self, n: int) -> int:
        fibon = [0,1]
        while len(fibon) < n:
            fibon.append(fibon[-2] + fibon[-1])
        return fibon[n-1]

if __name__ == "__main__":
    s = Fibonacci()

    assert s.solution(1) == 0
    print("Test on n=1 returns 0")
    assert s.solution(4) == 2
    print("Test on n=4 returns 2")
    assert s.solution(6) == 5
    print("Test on n=6 returns 5")
    assert s.solution(8) == 13
    print("Test on n=8 returns 13")

    # n_large = 10_000
    # time_limit = 1.0

    # start = time.perf_counter()
    # result = s.solution(n_large)
    # elapsed = time.perf_counter() - start

    # assert elapsed < time_limit, f"Too slow: {elapsed:.4f}s (limit: {time_limit}s)"