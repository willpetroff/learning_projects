def sieve_erat(limit, desired_prime=None):
    limit_plus = limit + 1
    list_one = [i for i in range(limit_plus)]
    list_one[1] = 0
    for i in range(2, int(limit ** .5) + 1):
        if list_one[i]:
            list_one[i * i:limit_plus:i] = [0] * len(range(i * i, limit_plus, i))
    if desired_prime:
        return list(filter(None, list_one))[desired_prime]
    else:
        return list(filter(None, list_one))


def main():
    prime_limit = int(input('please enter an integer: '))
    a = sieve_erat(prime_limit)
    sum_total = 0
    print(len(a))
    for i in a:
        sum_total += i
    print(sum_total)
    print(a)


main()
