# Excercise 10 - https://projecteuler.net/problem=10
'''
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
    Find the sum of all the primes below two million.

    Clarification: I considered below to be < and not <=
'''

def is_prime(n):
    ''' Returns True if n is prime else False '''
    nums_to_check = range(2, int(n**.5) + 1)
    for i in nums_to_check:
        if n % i == 0:
            return False
    return True



def find_all_primes(max_num = 100):
    ''' Returns list of all primes below (<) max_num '''
    primes =[]
    for num in range(2, max_num):
        if is_prime(num):
            primes.append(num)
    return primes


# Make a list of primes
primes = find_all_primes(max_num = 2000000)

# Print the sum
print('The sum of all primes below two million:', sum(primes))