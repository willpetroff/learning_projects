from random import randint
from time import time


def knap_max(item_weight, item_value, index, av_weight):
    if index == 0:
        if item_weight[index] <= av_weight:
            return item_value[index]
        else:
            return 0
    else:
        without_item = knap_max(item_weight, item_value, index-1, av_weight)
        if item_weight[index] > av_weight:
            return without_item
        else:
            with_item = item_value[index]+knap_max(item_weight, item_value, index-1, av_weight-item_weight[index])
        return max(with_item, without_item)


def fast_knap_max(item_weight, item_value, index, av_weight, call_back):
    try:
        return call_back[(index, av_weight)]
    except KeyError:
        if index == 0:
            if item_weight[index] <= av_weight:
                call_back[(index, av_weight)] = item_value[index]
                return item_value[index]
            else:
                call_back[(index, av_weight)] = 0
                return 0
        else:
            without_item = fast_knap_max(item_weight, item_value, index-1, av_weight, call_back)
            if item_weight[index] > av_weight:
                call_back[(index, av_weight)] = without_item
                return without_item
            else:
                with_item = item_value[index] + fast_knap_max(item_weight, item_value, index-1,
                                                              av_weight-item_weight[index], call_back)
            resolution = max(with_item, without_item)
            call_back[(index, av_weight)] = resolution
            return resolution


def main():
    items_avail_wght = []
    items_avail_valu = []
    for i in range(1, randint(50, 70)):
        a = randint(1, 8)
        b = randint(1, 12)
        items_avail_wght.append(a)
        items_avail_valu.append(b)
    allow_wght = randint(5, 35)
    index = len(items_avail_wght) - 1
    knap_memo = {}
    print(items_avail_wght)
    print(items_avail_valu)
    print(len(items_avail_wght), allow_wght)
    start_one = time()
    print(knap_max(items_avail_wght, items_avail_valu, index, allow_wght))
    end_one = time() - start_one
    start_two = time()
    print(fast_knap_max(items_avail_wght, items_avail_valu, index, allow_wght, knap_memo))
    end_two = time() - start_two
    print(end_one)
    print(end_two)

if __name__ == '__main__':
    main()
