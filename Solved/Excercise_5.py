# Excercise 5 - https://projecteuler.net/problem=5
'''
    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
evenly_divisble = []

for num in range(100000000,1000000000):
    noRemainder = True
    while noRemainder:
        for divisor_nums in range(1,21):
            if (num % divisor_nums) != 0:
                noRemainder = False
        else:
            break
    if noRemainder:
        evenly_divisble.append(num)

print(evenly_divisble) 
# Answer: 232792560