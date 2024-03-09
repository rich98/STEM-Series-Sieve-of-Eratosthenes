def sieve_of_eratosthenes(limit):
    primes = [True] * limit
    primes[0], primes[1] = False, False

    for ind, val in enumerate(primes):
        if val is True:
            primes[ind*2::ind] = [False] * (((limit - 1)//ind) - 1)

    return [ind for ind, val in enumerate(primes) if val is True]

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Generate prime numbers up to a smaller limit
limit =  1000000000                      
primes = sieve_of_eratosthenes(limit)

# Find two primes and add them together, then add 73
for i in range(len(primes)):
    for j in range(i+1, len(primes)):
        new_number = primes[i] + primes[j] + 73
        if new_number < limit and is_prime(new_number):
            print(f"The two primes are {primes[i]} and {primes[j]}, and the new number is {new_number}.")
            break
