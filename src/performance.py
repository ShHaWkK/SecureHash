import time
from .hash_algorithms import hash_password, hash_algorithms

def compare_performance():
    password = "test_password"
    results = {}
    for algo in hash_algorithms:
        start_time = time.time()
        for _ in range(1000):
            hash_password(password, algo)
        end_time = time.time()
        results[algo] = end_time - start_time
    return results
