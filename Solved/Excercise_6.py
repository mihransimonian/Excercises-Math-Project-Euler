# Excercise 6 - https://projecteuler.net/problem=6
'''
    The sum of the squares of the first ten natural numbers is; (1^2 + ... + 10^2) = 385
    The square of the sum of the first ten natural numbers is, (1+...+10) = 55^2 = 3025

    Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''
sum_of_squares = 0
square_of_sums = 0
difference = 0

for i in range(1,101):
    sum_of_squares += i**2

for i in range(1,101):
    square_of_sums += i
square_of_sums = square_of_sums**2

difference = square_of_sums - sum_of_squares

print('difference : ', difference)
# Answer: 25164150