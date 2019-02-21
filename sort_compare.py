#!/usr/bin/env python
# -*- coding utf-8 -*-
"""Assignment 4 Part 2"""


import time


def insertion_sort(a_list):
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
print(test1)


def shell_sort(a_list):
    start = time.time()
    
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)
        print("After increments of size", sublist_count, "The list is", a_list)
        sublist_count = sublist_count // 2

    end = time.time()

    return a_list, end - start
    
def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i
        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap

        a_list[position] = current_value
      
a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
test2 = shell_sort(a_list)
print(test2)


def python_sort(input_list):
    start = time.time()
    input_list.sort()
    end = time.time()
    return input_list, end - start

a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
test3 = python_sort(a_list)
print(test3)
   

