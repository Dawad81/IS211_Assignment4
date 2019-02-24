#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignment 4 Part 1."""


import time
import random


def sequential_search(a_list, item):
    """This is the Sequential Search Algorithm.
    Args:
        a_list (list): args to be serched for item.
        item (mixed): args to serch a_list for a match.
    Returns:
        tuple: returns a tuple with the first item in the tuple being a boolean
        (True/False) if item was found in a_list. The second item in the tuple
        is the time it took for the function to run.
    Example:
        >>> test_list1 = [1, 2, 32, 8, 17, 19, 42, 13, 0]
        >>> print sequential_search(test_list1, -1)
        (False, 4.0531158447265625e-06)
        >>> test_list1 = [1, 2, 32, 8, 17, 19, 42, 13, 0]
        >>> print sequential_search(test_list1, 42)
        (True, 5.9604644775390625e-06)
    """
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


def ordered_sequential_search(a_list, item):
    """This is the Ordered Sequential Search Algorithm.
    Args:
        a_list (list): args to be serched for item.
        item (mixed): args to serch a_list for a match.
    Returns:
        tuple: returns a tuple with the first item in the tuple being a boolean
        (True/False) if item was found in a_list. The second item in the tuple
        is the time it took for the function to run.
    Example:
        >>> test_list2 = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
        >>> print ordered_sequential_search(test_list2, -1)
        (False, 9.5367431640625e-07)
        >>> test_list2 = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
        >>> print ordered_sequential_search(test_list2, 17)
        (True, 5.9604644775390625e-06)
    """
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


def binary_search_iterative(a_list, item):
    """This is the Binary Search Iterative Algorithm.
    Args:
        a_list (list): args to be serched for item.
        item (mixed): args to serch a_list for a match.
    Returns:
        tuple: returns a tuple with the first item in the tuple being a boolean
        (True/False) if item was found in a_list. The second item in the tuple
        is the time it took for the function to run.
    Example:
        >>> test_list3 = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
        >>> print binary_search_iterative(test_list3, -1)
        (False, 3.0994415283203125e-06)
        >>> test_list3 = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
        >>> print binary_search_iterative(test_list3, 8)
        (True, 5.9604644775390625e-06)
    """
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


def binary_search_recursive(a_list, item):
    """This is the Binary Search Recursive Algorithm.
    Args:
        a_list (list): args to be serched for item.
        item (mixed): args to serch a_list for a match.
    Returns:
        tuple: returns a tuple with the first item in the tuple being a boolean
        (True/False) if item was found in a_list. The second item in the tuple
        is the time it took for the function to run.
    Example:
        >>> test_list4 = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
        >>> print binary_search_recursive(test_list4, -1)
        (False, 0.0)
        >>> test_list4 = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
        >>> print binary_search_recursive(test_list4, 42)
        (True, 9.5367431640625e-07)
    """
    a_list.sort()
    start = time.time()
    if len(a_list) == 0:
        end = time.time()
        found = False
    else:
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            end = time.time()
            found = True
        else:
            if item < a_list[midpoint]:
                return binary_search_recursive(a_list[:midpoint], item)
            else:
                return binary_search_recursive(a_list[midpoint + 1:], item)

    return found, end - start


def get_me_random_list(number):
    """Generates a list of number elements in random order.
    Args:
        number (int): Args to creat number of elements in the list
    Returns:
        list: A list with number elements in random order
    Example:
        >>> get_me_random_list(200)
        [186, 41, 145, 164, 13, 113, 44, 127, 32, 197, 193, 15, 23, 31, 73, 65,
        137, 159, 3, 14, 56, 80, 92, 133, 69, 190, 158, 116, 194, 198, 161, 91,
        20, 172, 62, 144, 106, 126, 109, 60, 101, 117, 105, 138, 10, 119, 83,
        78, 171, 136, 188, 128, 118, 199, 85, 98, 131, 59, 146, 17, 66, 9, 168,
        176, 114, 55, 37, 148, 77, 187, 11, 123, 156, 95, 16, 12, 86, 36, 110,
        147, 79, 181, 40, 141, 52, 50, 100, 166, 120, 75, 125, 89, 121, 170, 5,
        24, 122, 104, 90, 196, 47, 70, 132, 2, 139, 25, 96, 18, 195, 88, 183,
        108, 38, 51, 28, 43, 115, 130, 97, 162, 82, 174, 173, 61, 154, 93, 182,
        35, 4, 135, 94, 103, 8, 142, 68, 27, 84, 19, 160, 107, 0, 192, 140, 157,
        26, 112, 71, 53, 48, 87, 45, 134, 72, 111, 150, 177, 191, 58, 143, 54,
        151, 6, 30, 76, 102, 81, 34, 175, 178, 129, 57, 149, 67, 155, 99, 63,
        46, 152, 189, 169, 167, 184, 180, 49, 165, 185, 33, 64, 124, 21, 42, 29,
        179, 74, 7, 163, 1, 153, 22, 39]
    """
    r_list = range(number)
    random.shuffle(r_list)
    return r_list


def main():
    """This function test the run time of sequential_search(),
    ordered_sequential_search(), binary_search_iterative(),
    binary_search_recursive().
    Returns:
        5 str: for each item in list_size:
            str1: Length of the list of random numbers that was tested.
            str2: Average run time of sequential_search(), on 100 list of random
            numbers, of the length stated in str1.
            str3: Average run time of ordered_sequential_search(), on 100 list
            of random numbers, of the length stated in str1.
            str4: Average run time of binary_search_iterative(), on 100 list of
            random numbers, of the length stated in str1.
            str5: Average run time of binary_search_recursive(), on 100 list of
            random numbers, of the length stated in str1.
    Example:
        ========== List of 10000 random #'s: ==========
        Sequential Search took  0.0015114 seconds to run on average.
        Ordered Sequential Search took  0.0000013 seconds to run on average.
        Binary Search Iterative took  0.0000340 seconds to run on average.
        Binary Search Recursive took  0.0000002 seconds to run on average.
        ========== List of 500 random #'s: ==========
        Sequential Search took  0.0001981 seconds to run on average.
        Ordered Sequential Search took  0.0000005 seconds to run on average.
        Binary Search Iterative took  0.0000020 seconds to run on average.
        Binary Search Recursive took  0.0000002 seconds to run on average.
        ========== List of 1000 random #'s: ==========
        Sequential Search took  0.0001354 seconds to run on average.
        Ordered Sequential Search took  0.0000007 seconds to run on average.
        Binary Search Iterative took  0.0000021 seconds to run on average.
        Binary Search Recursive took  0.0000002 seconds to run on average.
    """
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
            run_time_total['Ordered_sequential'] += ordered_sequential_search(
                r_list, -1)[1]
            run_time_total['Binary_iterative'] += binary_search_iterative(
                r_list, -1)[1]
            run_time_total['Binary_recursive'] += binary_search_recursive(
                r_list, -1)[1]
            list_count -= 1
        print '=' * 10, "List of %s random #'s:" % test_list, '=' * 10
        print "Sequential Search took %10.7f seconds to run on average." % \
              float(run_time_total['Sequential'] / 100)
        print "Ordered Sequential Search took %10.7f seconds to run on average."\
              % float(run_time_total['Ordered_sequential'] / 100)
        print "Binary Search Iterative took %10.7f seconds to run on average."\
              % float(run_time_total['Binary_iterative'] / 100)
        print "Binary Search Recursive took %10.7f seconds to run on average."\
              % float(run_time_total['Binary_recursive'] / 100)


if __name__ == '__main__':
    main()
