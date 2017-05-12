"""
Find the sum of all "Ammicable Numbers" under 10000
"""

total = 0

def sum_of_perfect_divisors(num):
    divisors = [1]
    for i in range(2, int(num / 2) + 1):
        if num % i == 0:
            divisors.append(i)
    return sum(divisors)

for num in range(1, 10000):
    divisor_a = sum_of_perfect_divisors(num)
    if divisor_a < 10000 and divisor_a > num:
        divisor_b = sum_of_perfect_divisors(divisor_a)

        if divisor_b == num:
            print(divisor_a, divisor_b)
            total += (divisor_a + divisor_b)

print(total)