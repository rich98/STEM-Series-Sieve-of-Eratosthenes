def sieve_of_eratosthenes(limit):
    primes = [True] * limit
    primes[0], primes[1] = False, False
    prime_numbers = []

    for ind, val in enumerate(primes):
        if val is True:
            primes[ind*2::ind] = [False] * (((limit - 1)//ind) - 1)
            prime_numbers.append(ind)

    # Find pairs of primes that add up to another prime
    prime_pairs = []
    for i in range(len(prime_numbers)):
        for j in range(i+1, len(prime_numbers)):
            sum_of_primes = prime_numbers[i] + prime_numbers[j] + 1
            if sum_of_primes < limit and primes[sum_of_primes]:
                prime_pairs.append((prime_numbers[i], prime_numbers[j], sum_of_primes))
                if len(prime_pairs) == 5:
                    return prime_pairs

# Print prime pairs up to 1,000
prime_pairs = sieve_of_eratosthenes(1000)
for pair in prime_pairs:
    print(f"Prime {pair[0]} and Prime {pair[1]} add up to {pair[2]} which is also a prime.")
