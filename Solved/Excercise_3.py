# Excercise 3 - https://projecteuler.net/problem=3
'''
    The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143 ?

    Analysis of the given solution: 5*7*13*29 = 13195

    ## Definitions, source: mathisfun.com
    Prime num: A whole number greater than 1 that can not be made by multiplying other whole numbers
    Factor num: A factor that is a prime number. In other words: any of the prime numbers that can be multiplied to give the original number. (e.g. prime factors of 15 are 3 and 5)
'''
goal_num = 13195

# First make a list of primes
primes = []
for possible_prime in range(3, goal_num+1):
    # assume is prime, until found that it is not
    isPrime = True
    for num in range(2, possible_prime):
        if possible_prime % num == 0:
            isPrime = False
    if isPrime:
        primes.append(possible_prime)

# Caclulate the prime factors
prime_factors = []
for i in range(0, len(primes)):
    # see whether it is a full number after division
    # if not it is not the correct prime factor
    try:
        while (goal_num/primes[i]).is_integer() == False:
            primes.pop(i)
        prime_factors.append(primes[i])
    except:
        continue

print('prime factors : ', prime_factors)
# Answer:  [5, 7, 13, 29]