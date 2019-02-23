#!/usr/bin/env python
# -*- coding utf-8 -*-
"""Assignment 4 Part 2"""

import random
import time


def insertion_sort(a_list):
    """Docstring."""
    start = time.time()
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index
        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1
            a_list[position] = current_value
    end = time.time()
    return a_list, end - start

a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
test1 = insertion_sort(a_list)
print test1


def shell_sort(a_list):
    """Docstring."""
    start = time.time()

    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)
        #print("After increments of size", sublist_count, "The list is", a_list)
        sublist_count = sublist_count // 2

    end = time.time()

    return a_list, end - start

def gap_insertion_sort(a_list, start, gap):
    """Docstring."""
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i
        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap

        a_list[position] = current_value

a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
test2 = shell_sort(a_list)
print test2


def python_sort(input_list):
    """Docstring."""
    start = time.time()
    input_list.sort()
    end = time.time()
    return input_list, end - start

a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
test3 = python_sort(a_list)
print test3


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
        run_time_total = {'Insertion Sort': 0,
                          'Shell Sort': 0,
                          'Python Sort': 0}
        while list_count > 0:
            run_time_total['Insertion Sort'] += insertion_sort(r_list)[1]
            run_time_total['Shell Sort'] += shell_sort(r_list)[1]
            run_time_total['Python Sort'] += python_sort(r_list)[1]
            list_count -= 1
        print "List of %s random #'s:" % test_list
        print "Insertion Sort took %10.7f seconds to run on average." % float(run_time_total['Insertion Sort'] / 100)
        print "Shell Sort took %10.7f seconds to run on average." % float(run_time_total['Shell Sort'] / 100)
        print "Python Sort took %10.7f seconds to run on average." % float(run_time_total['Python Sort'] / 100)


if __name__ == '__main__':
    main()
