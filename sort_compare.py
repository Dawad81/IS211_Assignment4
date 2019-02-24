#!/usr/bin/env python
# -*- coding utf-8 -*-
"""Assignment 4 Part 2"""

import random
import time


def insertion_sort(a_list):
    """This is the Insertion Sort Algorithm.

    Args:
        a_list (list): args to be sorted.

    Returns:
        tuple: returns a tuple with the first item in the tuple being a_list
        sorted. The second item in the tuple is the time it took for the
        function to run.

    Example:
        >>> a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
        >>> insertion_sort(a_list)
        ([17, 20, 26, 31, 44, 54, 55, 77, 93], 1.0967254638671875e-05)
    """
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


def shell_sort(a_list):
    """This is the Shell Sort Algorithm.

    Args:
        a_list (list): args to be sorted.

    Returns:
        tuple: returns a tuple with the first item in the tuple being a_list
        sorted. The second item in the tuple is the time it took for the
        function to run.

    Example:
        >>> a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
        >>> shell_sort(a_list)
        ([17, 20, 26, 31, 44, 54, 55, 77, 93], 2.8133392333984375e-05)
    """
    start = time.time()
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)
        sublist_count = sublist_count // 2
    end = time.time()
    return a_list, end - start


def gap_insertion_sort(a_list, start, gap):
    """To be called within the shell_sort algorithm."""
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i
        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap
        a_list[position] = current_value


def python_sort(input_list):
    """This is the Python Sort Algorithm.

    Args:
        a_list (list): args to be sorted.

    Returns:
        tuple: returns a tuple with the first item in the tuple being a_list
        sorted. The second item in the tuple is the time it took for the
        function to run.

    Example:
        >>> a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
        >>> python_sort(a_list)
        ([17, 20, 26, 31, 44, 54, 55, 77, 93], 4.0531158447265625e-06)
    """
    start = time.time()
    input_list.sort()
    end = time.time()
    return input_list, end - start


def get_me_random_list(number):
    """Generates a list of number elements in random order.

    Args:
        number (int): Args to creat number of elements in the list.

    Returns:
        list: A list with number elements in random order.

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
    """This function test the run time of insertion_sort(), shell_sort(),
    python_sort().

    Returns:
        4 str: for each item in list_size:
            str1: Length of the list of random numbers that was tested.

            str2: Average run time of insertion_sort(), on 100 list of random
            numbers, of the length stated in str1.

            str3: Average run time of shell_sort(), on 100 list
            of random numbers, of the length stated in str1.

            str4: Average run time of python_sort(), on 100 list of
            random numbers, of the length stated in str1.

    Example:
        ========== List of 10000 random #'s: ==========
        Insertion Sort took  0.0404678 seconds to run on average.
        Shell Sort took  0.0210525 seconds to run on average.
        Python Sort took  0.0001041 seconds to run on average.
        ========== List of 500 random #'s: ==========
        Insertion Sort took  0.0002338 seconds to run on average.
        Shell Sort took  0.0010097 seconds to run on average.
        Python Sort took  0.0000063 seconds to run on average.
        ========== List of 1000 random #'s: ==========
        Insertion Sort took  0.0007305 seconds to run on average.
        Shell Sort took  0.0018530 seconds to run on average.
        Python Sort took  0.0000125 seconds to run on average.

    """
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
        print '=' * 10, "List of %s random #'s:" % test_list, '=' * 10
        print "Insertion Sort took %10.7f seconds to run on average." % float(
            run_time_total['Insertion Sort'] / 100)
        print "Shell Sort took %10.7f seconds to run on average." % float(
            run_time_total['Shell Sort'] / 100)
        print "Python Sort took %10.7f seconds to run on average." % float(
            run_time_total['Python Sort'] / 100)


if __name__ == '__main__':
    main()
