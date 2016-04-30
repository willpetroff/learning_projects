def sqrt_int(x):
    ans = 0
    if x >= 0 and type(x) == int:
        while ans * ans < x:
            ans += 1
        if ans * ans != x:
            print('Sorry, ' + str(x) + ' is not a perfect square, starting float test')
            sqrt_float(float(x), .000001)
        else:
            print('The square root of ' + str(x) + ' is ' + str(ans) + '.')
    elif x < 0:
        print('The number you are seeking is most certainly imaginary.'
              ' If you persist in your efforts to try and find it, it might be best to look for it in a padded room')


def sqrt_float(x, epsilon):
    if x >= 1 and type(x) == float:
        guess = x / 2.0
        counter = 0
        if abs(guess ** 2 - x) > epsilon:
            while abs(guess ** 2 - x) > epsilon and counter <= 10000:
                guess -= ((guess ** 2 - x) / (2.0 * guess))
                counter += 1
        else:
            print(guess)
        print(counter - 1, guess, guess * guess)
    elif x < 1 and type(x) == float:
        low = 0.0
        high = max(x, 1.0)
        guess = (low + high) / 2.0
        counter = 0
        if abs(guess ** 2 - x) > epsilon:
            while abs(guess ** 2 - x) > epsilon and counter <= 10000:
                if guess ** 2 < x:
                    low = guess
                else:
                    high = guess
                guess = (low + high) / 2.0
                counter += 1
        else:
            print(guess)
            return guess
        print(counter - 1, guess, guess * guess)
        if counter > 10000:
            print('Counter timed out.')


def main():
    print('This is a small test program to find the square root of a number.')
    user_input = input('Please input a number: ')
    test_value = True
    for char in user_input:
        if char.isdigit() == True or char == '.' and user_input.count('.') <= 1:
            test_value = True
        else:
            print('You naughty minx, you. You\'ve entered an input that isn\'t allowed!')
            return False
    if test_value:
        if '.' in user_input:
            user_input = float(user_input)
            sqrt_float(user_input, .0000001)
        else:
            user_input = int(user_input)
            sqrt_int(user_input)
    
    
if __name__ == '__main__':
    main()
