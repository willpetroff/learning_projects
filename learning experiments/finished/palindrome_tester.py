"""
This script takes a string input from the user and tests to see if it's a palindrome.
"""


def pal_test(string):
    if len(string) <= 1:
        return True  # Returns true if the string is a single character or less
    else:
        test = True  # Sets test default to True
        for letter in range(0, len(string)):
            # Compares character in place "x" to it's opposite character in place "-x"
            if string[letter] != string[len(string) - 1 - letter]:
                test = False  # Sets test value to False if letter X doesn't equal letter -X
                break  # Breaks out of the loop after False value set
    if test:
        return True
    else:
        return False


def pal_test_recur(string):  # Uses recursion to solve the problem instead of looping through
    if len(string) <= 1:  # Returns true if the string is a single character or less
        return True
    else:
        if string[0] == string[len(string) - 1]:  # Checks to see if character X is equal to character -X
            # If True, the function calls itself with the string concatenated by one space at both front and end
            return pal_test_recur(string[1:len(string) - 1])
        else:
            return False


def main():
    pal_string = input('Please enter a word for the test: ')
    a = pal_test(pal_string)
    b = pal_test_recur(pal_string)
    print(a, b)
main()
