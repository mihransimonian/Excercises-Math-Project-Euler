# Excercise 16 - https://projecteuler.net/problem=16
'''
    2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
    What is the sum of the digits of the number 2^1000?
'''
def calculate_sum_of_digits(digits):
    sum = 0
    for num in str(digits)[::1]:
        try:
            sum += int(num)
        except:
            pass
    return sum

digits = 2**1000
#print('2^1000 equals : ', digits)

print('the sum of the digits equals : ', calculate_sum_of_digits(digits))
# Answer: 1366