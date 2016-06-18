"""
Finds the sum of the digits in a given factorial.
"""


def fact_math(num):
    """
    returns the factorial of a given number
    :param num: int value num
    :return: int value
    """
    if num == 1:
        return 1
    else:
        return num * fact_math(num-1)

a = fact_math(100)
print(sum([int(i) for i in str(a)]))
