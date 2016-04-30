"""
This script takes a number input from the user and searches a list to see if the number given is in the list
"""

from time import time


def create_list():
    new_list = [i for i in range(10000000)]
    return new_list


def bi_search(search_term, input_list):  # Takes the user input and generated list
    input_list.sort()  # Sorts the list
    # print (input_list)
    first = 0  # Sets index value of the first item in the list
    last = len(input_list) - 1  # Sets the index value of the last item in the list
    mid_point = int(first + ((first + last) / 2))  # Sets the index value for the middle of the list
    # print (input_list[mid_point])
    if len(input_list) <= 2:  # Checks to see if the given list contains two or fewer items
        if input_list[0] == search_term or input_list[1] == search_term:
            return True
        else:
            return False
    else:
        if input_list[mid_point] != search_term:  # Checks to see if the value at mid-point is equal to the user input
            if input_list[mid_point] > search_term:
                # If the value at mid-point is greater than the user input, this sets index value of the last item
                # to the current mid-point index value
                last = mid_point
            else:
                # If the value at mid-point is less than the user input, this sets index value of the first item
                # to the current mid-point index value
                first = mid_point
            # print (first, last)
            return bi_search(search_term, input_list[first:last + 1])  # Calls itself with the halved list as a value
        else:
            return True


def main():
    new_list = create_list()
    num_search = int(input('Please enter a number: '))
    start_time = time()
    ans = bi_search(num_search, new_list)
    end_time = time() - start_time
    if ans:
        print('True')
    else:
        print('False')
    print(end_time)


if __name__ == '__main__':
    main()
