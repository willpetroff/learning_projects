from time import time


def prime_generator(upper_limit, stop_len):
    prime_list = []
    while len(prime_list) != stop_len:
        for i in range(2, upper_limit + 1):
            for p in range(2, int(i / 2) + 1):
                if i % p == 0:
                    break
            else:
                prime_list.append(i)
        return prime_list
    return prime_list


def div_list_generator(upper_limit):
    dict_of_divs = {}
    for i in range(2, upper_limit + 1):
        if i < 3:
            lim = 3
            list_of_divs = []
        elif i == 3:
            lim = 3
            list_of_divs = [i]
        else:
            lim = int(i / 2) + 1
            list_of_divs = [i]
        for p in range(1, lim):
            if i % p == 0:
                list_of_divs.append(p)
            a = sorted(list_of_divs)
            dict_of_divs[i] = a
    return dict_of_divs


def main():
    input_success = False
    user_input_lim = input('Please enter an integer: ')
    while input_success is False:
        if not user_input_lim.isdigit():
            user_input_lim = input('You did not enter an integer, please try again: ')
        else:
            user_input_lim = int(user_input_lim)
            input_success = True
    user_input_stop = int(input('please enter an integer: '))
    # a=div_list_generator(user_input_lim)
    b = prime_generator(user_input_lim, user_input_stop)
    print(b[user_input_stop])


main()
