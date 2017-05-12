def fibb_sum(lim):
    first_num = 1
    last_num = 2
    even_sum = 0
    while last_num <= lim:
        temp_sum = first_num
        first_num = last_num
        if last_num % 2 == 0:
            even_sum += last_num
        last_num = first_num + temp_sum
    return even_sum


if __name__ == '__main__':
    user_input = int(input('enter integer: '))
    a = fibb_sum(user_input)
    print(a)
