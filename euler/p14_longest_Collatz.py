largest_seq = 0
count = 2
while count < 1000000:
    value = count
    seq_count = 0
    while value > 1:
        if value%2 == 0:
            value = value//2
        else:
            value = (3*value)+1
        seq_count += 1
    if seq_count > largest_seq:
        largest_seq = seq_count
        print(count, largest_seq)
    count += 1