"""
This script show the difference (in run-time) in assigning an unchanging value to a variable vs constantly calling a function to
determine the value as needed
"""

from time import time


def call_1():
    a = [i for i in range(10000000)]
    counter = 0
    start_time = time()
    while counter < len(a):  # Constantly calls len() function to determine the value
        counter += 1
    end_time = time() - start_time
    print(end_time)


def call_2():
    a = [i for i in range(10000000)]
    counter = 0
    a_len = len(a)  # Sets the value of 'a_len' to len(a)
    start_time = time()
    while counter < a_len:  # Avoids constant calls to len() function
        counter += 1
    end_time = time() - start_time
    print(end_time)


def main():
    call_1()
    call_2()


if __name__ == '__main__':
    main()
