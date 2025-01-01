# 1007 素数对猜想
def generate_prime(n):
    is_prime = [True]*(n+1)
    is_prime[0] = is_prime[1] = False
    p = 2
    while p*p <= n:
        if is_prime[p]:
            for i in range(p*p, n+1, p):
                is_prime[i] = False
        p += 1
    return [i for i in range(2, n+1) if is_prime[i]]
    

def solution():
    n = int(input())
    primes = generate_prime(n)
    count = 0
    for i in range(1, len(primes)):
        if primes[i] - primes[i-1] == 2:
            count += 1
    print(count)
    return

if __name__ == "__main__":
    solution()
