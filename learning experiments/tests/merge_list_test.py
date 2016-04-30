from random import random
from time import time

def split_lists(big_list):
    list_len=len(big_list)
    if list_len<2:
        return big_list
    mid=(list_len-1)/2

def merge_lists(list_one, list_two):
    new_list=[]
    len_one=len(list_one)
    len_two=len(list_two)
    counter_one=0
    counter_two=0
    while counter_one<len_one and counter_two<len_two:
        if list_one[counter_one]<list_two[counter_two]:
            new_list.append(list_one[counter_one])
            counter_one+=1
        else:
            new_list.append(list_two[counter_two])
            counter_two+=1
        print (counter_one, counter_two, new_list)
    if (len_one-counter_one)>(len_two-counter_two):
        while counter_one<len_one:
            new_list.append(list_one[counter_one])
            counter_one+=1
            print (counter_one, counter_two, new_list)
    if (len_two-counter_two)>(len_one-counter_one):
        while counter_two<len_two:
            new_list.append(list_two[counter_two])
            counter_two+=1
            print (counter_one, counter_two, new_list)
    return new_list


def main():
    a=[]
    b=[]
    for i in range(100):
        if i%2==0:
            a.append(i)
        else:
            b.append(i)
    #print (a)
    #print (b)
    start_time=time()
    c=merge_lists(a,b)
    end_time=time()-start_time
    print (end_time)


main()
