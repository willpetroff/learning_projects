def larg_fact(given_int):
    test_list = []
    factor_num = 2
    while factor_num <= given_int:
        if given_int % factor_num == 0:
            given_int /= factor_num
            test_list.append(factor_num)
        else:
            factor_num += 1
    return test_list


def main():
    user_input = int(input('enter int: '))
    a = larg_fact(user_input)
    b = sorted(a)
    print(b)
    print(b[-1])

main()
