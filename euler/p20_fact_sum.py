def fact_math(num):
    if num == 1:
        return 1
    else:
        return num * fact_math(num-1)

a = fact_math(100)
print(sum([int(i) for i in str(a)]))