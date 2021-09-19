#!/usr/bin/python3


def uniq_add(my_list=[]):
    list2 = []
    for i in my_list:
        if i not in list2:
            list2.append(i)
    return sum(list2)
