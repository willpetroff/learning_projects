def pyth_trip():
    for a in range(1, 1001):
        for b in range(1, 1001):
            for c in range(1, 1001):
                if a < b and b < c:
                    pyth_sum = (a ** 2) + (b ** 2)
                    if pyth_sum == c ** 2 and (a + b + c) == 1000:
                        return a, b, c
                    else:
                        pass
                else:
                    pass


def main():
    print(pyth_trip())
