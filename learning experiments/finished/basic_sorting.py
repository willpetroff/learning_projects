"""
This is a file that contains various sorting algorithms.
"""


from random import randint


def selection_sort(input_list):
    for initial_index_value in range(len(input_list)):
        min_value = input_list[initial_index_value]  # Sets first list item as minimum value
        min_value_index = initial_index_value  # Sets initial index value for smallest number/char
        for unsorted_index_value in range((initial_index_value + 1), len(input_list)):  # Runs through remaining list
            if min_value > input_list[unsorted_index_value]:
                # If a item later in the list is smaller, a new minimum value is set, along with a new index value
                min_value = input_list[unsorted_index_value]
                min_value_index = unsorted_index_value
        if min_value == input_list[initial_index_value]:
            # If the minimum value is the same as the current value, no change is needed
            pass
        else:
            # If the minimum value is smaller than the current value, the two values ar swapped
            temp_value = input_list[initial_index_value]
            input_list[initial_index_value], input_list[min_value_index] = min_value, temp_value


def bubble_sort(input_list):
    no_changes = False  # Sets default value to False
    last_index_counter = 1
    while not no_changes:
        no_changes = True  # Switches default value to True and assumes no changes will be made
        for i in range(len(input_list)-last_index_counter):  # Iterates through all but the last index value of the list
            # Compares the value at a given index value to the one immediately after it
            if input_list[i] > input_list[i + 1]:
                # If the current index value item is larger than the next index value item, the two are swapped
                input_list[i], input_list[i + 1] = input_list[i + 1], input_list[i]
                no_changes = False  # Resets the default value to False if change was made to keep the loop going
        last_index_counter += 1  # Increment last_index_counter by one, knowing that the last element is the largest


def insertion_sort(input_list):
    for index_value in range(1, len(input_list)):
        value = input_list[index_value]
        value_index = index_value
        while value_index > 0 and input_list[value_index - 1] > value:  # Compare each value to the previous value
            # If possible, and if the previous value is larger, swap the two values
            input_list[value_index], input_list[value_index - 1] = input_list[value_index - 1], value
            value_index -= 1  # Move the value_index counter back one level


def main():
    test_list_1 = [randint(1, 10000) for _ in range(1000)]
    selection_sort(test_list_1)
    print(test_list_1)
    test_list_2 = [randint(1, 10000) for _ in range(1000)]
    bubble_sort(test_list_2)
    print(test_list_2)
    test_line_3 = [randint(1, 10000) for _ in range(1000)]
    insertion_sort(test_line_3)
    print(test_line_3)


if __name__ == "__main__":
    main()
