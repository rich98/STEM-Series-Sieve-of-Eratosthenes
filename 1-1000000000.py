def sieve_of_eratosthenes(limit):
    primes = [True] * limit
    primes[0], primes[1] = False, False

    for ind, val in enumerate(primes):
        if val is True:
            print(ind)  # Print the prime number as it is found
            primes[ind*2::ind] = [False] * (((limit - 1)//ind) - 1)

# Print prime numbers up to 1,000,000,000
# WARNING: This will take a significant amount of time and memory.
sieve_of_eratosthenes(1000000000)
