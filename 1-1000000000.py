def sieve_of_eratosthenes(limit):
    primes = [True] * limit
    primes[0], primes[1] = False, False

    for ind, val in enumerate(primes):
        if val is True:
            primes[ind*2::ind] = [False] * (((limit - 1)//ind) - 1)

    return [ind for ind, val in enumerate(primes) if val is True]

# Print prime numbers up to 1 billion 
# WARNING: This will take a significant amount of time and memory.
primes = sieve_of_eratosthenes(1000000000)
for prime in primes:
    print(prime)
