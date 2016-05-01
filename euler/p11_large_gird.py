import csv


def grid_search(grid_csv):
    grid_arr = []
    product_list = []
    with open(grid_csv, 'r') as array_grid:
        reader = csv.reader(array_grid)
        for line in reader:  # takes line from csv file and adds it to array
            grid_line = line[0].split()
            grid_arr.append(grid_line)
        for row in grid_arr:  # converts string numbers into int numbers
            for index in range(len(row)):
                row[index] = int(row[index])
    for row_val in range(len(grid_arr)):
        for col_val in range(len(grid_arr[row_val])):  # appends product values to master list
            product_list.append(prod_across(grid_arr, row_val, col_val))
            product_list.append(prod_down(grid_arr, row_val, col_val))
            product_list.append(prod_diagonal_left(grid_arr, row_val, col_val))
            # index values need to have enough depth to not draw on negative index values
            if col_val > 2 and row_val > 2:
                product_list.append(prod_diagonal_right(grid_arr, row_val, col_val))
    product_list.sort()  # sorts master list
    return product_list[-1]  # returns last (largest) value from master list


def prod_across(given_arr, row_index, col_index):
    final_prod = 0
    try:
        final_prod = given_arr[row_index][col_index] * given_arr[row_index][col_index+1] * \
                     given_arr[row_index][col_index+2] * given_arr[row_index][col_index+3]
    except IndexError:  # excepts out-of-bounds error for list indices
        pass
    return final_prod


def prod_down(given_arr, row_index, col_index):
    final_prod = 0
    try:
        final_prod = given_arr[row_index][col_index] * given_arr[row_index+1][col_index] * \
                     given_arr[row_index+2][col_index] * given_arr[row_index+3][col_index]
    except IndexError:
        pass
    return final_prod


def prod_diagonal_left(given_arr, row_index, col_index):  # calculates diagonal array forward
    final_prod = 0
    try:
        final_prod = given_arr[row_index][col_index] * given_arr[row_index+1][col_index+1] * \
                     given_arr[row_index+2][col_index+2] * given_arr[row_index+3][col_index+3]
    except IndexError:
        pass
    return final_prod


def prod_diagonal_right(given_arr, row_index, col_index):  # calculates diagonal array backwards
    final_prod = 0
    try:
        final_prod = given_arr[row_index][col_index] * given_arr[row_index+1][col_index-1] * \
                     given_arr[row_index+2][col_index-2] * given_arr[row_index+3][col_index-3]
    except IndexError:
        pass
    return final_prod


grid = 'C:\\Users\\William\\Desktop\\euler_array.csv'
final_answer = grid_search(grid)
print(final_answer)
