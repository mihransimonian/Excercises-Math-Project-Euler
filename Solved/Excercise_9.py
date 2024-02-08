# Excercise 9 - https://projecteuler.net/problem=9
# This works, but it does not meet a < b, as the result is a > b
'''
    A Pythagorean triplet is a set of three natural numbers, a < b < c, for which; a^2 + b^2 = c^2
        For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.


    Natural number: A whole number so no decimals etc, also no negatives

    Pythagorean Triples: 
    Source: https://www.mathsisfun.com/numbers/pythagorean-triples.html
    Properties:
        An interesting fact: a Pythagorean Triple always consists of:
        - all even numbers, or
        - two odd numbers and an even number.

    A Pythagorean Triple can never be made up of all odd numbers or two even numbers and one odd number. This is true because:

    So, when both a and b are even, c is even too. Similarly when one of a and b is odd and the other is even, c has to be odd!

    Constructing Pythagorean Triples:
    When m and n are any two positive integers (m > n):
        a = m2 − n2
        b = 2mn
        c = m2 + n2
'''

def calc_a_b_c_from_m_n(m, n):
    a = (m**2) - (n**2)
    b = (2 * m * n)
    c = (m**2) + (n**2)
    return (a, b, c)


def find_pythagorean_triplet(goal_abc_sum=1000):
    for m in range(2, 64):
        # assure m > n by placing m above n
        for n in range(m, 0, -1):
            (a, b, c) = calc_a_b_c_from_m_n(m=m, n=n)
            abc_sum = (a + b + c)
            if abc_sum == goal_abc_sum:
                return (a, b, c, abc_sum, m, n)
    # Error handling
    raise Exception('Error, the goal_abc_sum cannot be found')


(a, b, c, abc_sum, m, n) = find_pythagorean_triplet(goal_abc_sum=1000)
print('With parameters a:', a, 'b:', b, 'and c:', c, '\nThe sum of abc is:', abc_sum, 'with product abc:', (a*b*c), 'with parameters m:', m, 'and n:', n)