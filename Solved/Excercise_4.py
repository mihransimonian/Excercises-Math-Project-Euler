# Excercise 4 - https://projecteuler.net/problem=4
'''
    A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
    Find the largest palindrome made from the product of two 3-digit numbers.
'''
palindromic_numbers = []

for a in range(100,1000):
    for b in range(100,1000):
        c = str(a*b)
        if c == c[::-1]:
            palindromic_numbers.append(a*b)

# reduce size
palindromic_numbers = list(set(palindromic_numbers))
palindromic_numbers.sort()

# print result
print(palindromic_numbers[-1])
# Answer: 906609