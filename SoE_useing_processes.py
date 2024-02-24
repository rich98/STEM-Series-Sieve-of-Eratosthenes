import concurrent.futures

def sieve_of_eratosthenes(limit):
    primes = [True] * limit
    primes[0], primes[1] = False, False

    def mark_false(i):
        if primes[i] is True:
            primes[i*2::i] = [False] * (((limit - 1)//i) - 1)

    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(mark_false, (i for i in range(2, int(limit**0.5) + 1)))

    for i, val in enumerate(primes):
        if val is True:
            print(i)  # Print the prime number as it is found

# Print prime numbers up to 1,000,000,000
# WARNING: This will take a significant amount of time and memory.
sieve_of_eratosthenes(1000000000)
