"""
Modular approach to FizzBuzz Problem
"""


def fizz_buzz_mod(count, *args):
    """
    :param count: int --> Target number to cycle through to
    :param args: variable number of tuples (or lists, or sets) --> (int divisor, str word to print)
    :return: Nothing; results printed during loop
    """
    sorted_args = sorted(args, key=lambda x: x[0])
    for i in range(1, count + 1):
        print_string = ""
        for arg in sorted_args:
            if i % arg[0] == 0:
                print_string += arg[1]
        print(print_string if print_string else i)


if __name__ == "__main__":
    fizz_buzz_mod(30, (6, 'Pop'), (3, 'Fizz'), (5, 'Buzz'))
