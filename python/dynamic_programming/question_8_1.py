"""
Triple Step:
    A child is running up a staircase with n steps and can hope either 1 step,
    2 steps, or 3 steps at a time. Implement a method to count how many possible ways
    the child can run up the stairs.

"""
import sys

def solution(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    
    return solution(n - 1) + solution(n - 2) + solution(n - 3)
    

def memoized_solution(n, cache=None):
    if cache is None:
        cache = {}
    
    if n < 0:
        return 0
    
    if n == 0:
        return 1
    
    elif cache.get(n):
        return cache[n]
    
    cache[n] = (
        memoized_solution(n - 1, cache) + 
        memoized_solution(n - 2, cache) + 
        memoized_solution(n - 3, cache)
    )
    return cache[n]        


if __name__ == "__main__":
    print("Result: ", memoized_solution(int(sys.argv[1])))
