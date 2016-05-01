def str_num_con(text_path):
    arr = []
    with open(text_path, 'r') as text_file:
        for line in text_file:
            arr.append(int(line.strip()))
    return arr





num_string = 'C:\\Users\\William\\Documents\\Python Projects\\euler_files\\p13_large_sum.txt'
num_arr = str_num_con(num_string)
print(str(sum(num_arr))[:10])
