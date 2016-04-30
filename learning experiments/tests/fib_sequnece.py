from time import time


def fib_sequence(levels_out):
    if levels_out == 0:
        return 1
    elif levels_out == 1:
        return levels_out
    else:
        return fib_sequence(levels_out - 1) + fib_sequence(levels_out - 2)


def fast_fib_sequence(levels_out, dict_of_levels):
    if levels_out not in dict_of_levels:
        dict_of_levels[levels_out] = fast_fib_sequence(levels_out - 1, dict_of_levels) +\
                                     fast_fib_sequence(levels_out - 2, dict_of_levels)
    return dict_of_levels[levels_out]


def fast_fib_seeder(levels_out):
    dict_of_levels = {0: 1, 1: 1}
    return fast_fib_sequence(levels_out, dict_of_levels)


def main():
    number = int(input('Please enter the level you would like to calculate out to: '))
    start_one = time()
    print(fib_sequence(number))
    end_one = time() - start_one
    start_two = time()
    print(fast_fib_seeder(number))
    end_two = time() - start_two
    print(end_one)
    print(end_two)

if __name__ == '__main__':
    main()
