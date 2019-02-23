#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignment 4 Part 1."""


import time
import random


def sequential_search(a_list, item):
    """Docstring."""
    start = time.time()
    pos = 0
    found = False
    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos+1
    end = time.time()
    return found, end - start

test_list1 = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print sequential_search(test_list1, -1)
print sequential_search(test_list1, -1)


def ordered_sequential_search(a_list, item):
    """Docstring."""
    a_list.sort()
    start = time.time()
    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos+1
    end = time.time()
    return found, end - start

test_list2 = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print ordered_sequential_search(test_list2, -1)
print ordered_sequential_search(test_list2, -1)


def binary_search_iterative(a_list, item):
    """Docstring."""
    a_list.sort()
    start = time.time()
    first = 0
    last = len(a_list) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    end = time.time()
    return found, end - start

test_list3 = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print binary_search_iterative(test_list3, -1)
print binary_search_iterative(test_list3, -1)


def binary_search_recursive(a_list, item):
    """Docstring."""
    a_list.sort()
    start = time.time()
    if len(a_list) == 0:
        end = time.time()
        found = False #, end - start
    else:
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            end = time.time()
            found = True #, end - start
        else:
            if item < a_list[midpoint]:
                return binary_search_recursive(a_list[:midpoint], item)
            else:
                return binary_search_recursive(a_list[midpoint + 1:], item)

    return found, end - start

test_list4 = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print binary_search_recursive(test_list4, -1)
print binary_search_recursive(test_list4, -1)


def get_me_random_list(number):
    """Generate list of n elements in random order
    :params: n: Number of elements in the list
    :returns: A list with n elements in random order
    """

    r_list = range(number)
    random.shuffle(r_list)
    return r_list

test_random = get_me_random_list(200)
print test_random


def main():
    """Docstring."""
    list_size = dict(list_size500=500, list_size1k=1000, list_size10k=10000)
    for test_list in list_size.values():
        r_list = get_me_random_list(test_list)
        list_count = 100
        run_time_total = {'Sequential': 0,
                          'Ordered_sequential': 0,
                          'Binary_iterative': 0,
                          'Binary_recursive': 0}
        while list_count > 0:
            run_time_total['Sequential'] += sequential_search(r_list, -1)[1]
            run_time_total['Ordered_sequential'] += ordered_sequential_search(r_list, -1)[1]
            run_time_total['Binary_iterative'] += binary_search_iterative(r_list, -1)[1]
            run_time_total['Binary_recursive'] += binary_search_recursive(r_list, -1)[1]
            list_count -= 1
        print "List of %s random #'s:" % test_list
        print "Sequential Search took %10.7f seconds to run on average." % float(run_time_total['Sequential'] / 100)
        print "Ordered Sequential Search took %10.7f seconds to run on average." % float(run_time_total['Ordered_sequential'] / 100)
        print "Binary Search Iterative took %10.7f seconds to run on average." % float(run_time_total['Binary_iterative'] / 100)
        print "Binary Search Recursive took %10.7f seconds to run on average." % float(run_time_total['Binary_recursive'] / 100)


if __name__ == '__main__':
    main()
