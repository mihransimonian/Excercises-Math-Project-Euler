# Excercise 48 - https://projecteuler.net/problem=48
'''
    The series, 1^1 + 2^2 + ... + 10^10 = 10405071317.
    Find the last ten digits of the series, 1^1 + 2^2 + ... + 1000^1000.
'''
total = 0

for num in range(1,1001):
    total += (num**num)

print('last ten digits', str(total)[-10:])
# Answer: last ten digits 9110846700