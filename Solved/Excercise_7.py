# Excercise 7 - https://projecteuler.net/problem=7
'''
    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
    What is the 10 001st prime number?
'''
primes = []

for possible_prime in range(3, 9999999999):
    # assume is prime, until found that it is not
    isPrime = True
    for num in range(2, possible_prime):
        if possible_prime % num == 0:
            isPrime = False
    if isPrime:
        primes.append(possible_prime)
    if len(primes) > 10001:
        break

print(primes[-2])
# Answer: 104743