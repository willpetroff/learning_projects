from random import randint

def rand_sort(orig_list, count=0):
    copy_list = orig_list[::]
    sorted_list = []
    while copy_list:
        index = randint(0, len(copy_list)-1)
        if copy_list[index] not in sorted_list:
            sorted_list.append(copy_list[index])
            copy_list = copy_list[:index] + copy_list[index + 1:]
    if sorted_list == orig_list:
        return count
    else:
        new_count = count + 1
        return rand_sort(orig_list, new_count)


if __name__ == "__main__":
    list_of_counts = []
    for _ in range(100):
        list_of_counts.append(rand_sort([1,2,3,4,5]))
    for index in range(10):
        print(list_of_counts[index:index + 10])
    print(sum(list_of_counts)/100)