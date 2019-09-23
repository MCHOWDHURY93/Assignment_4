#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""Assignment_4, Part 2"""

import time
import random


def insertion_sort(a_list):
    """A algorithm that sorts a list and returns the processing time and the
    sorted list.
    Args:
        a_list(list): A list of any data type.
    Returns:
        (tuple): A tuple containing the processing time and the list, sorted.
    Example:
        >>> b = list_gen(10)
        >>> insertion_sort(b)
        (1.0013580322265625e-05, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    """
    strt_time = time.time()

    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1

        a_list[position] = current_value

    end_time = time.time()

    run_time = end_time - strt_time

    return (run_time, a_list)


def gap_insertion_sort(a_list, start, gap):
    """An algorithm that sorts a list using the gap insertion method.
    Args:
        a_list(list): a list of items to be sorted.
        start(int): The starting position for the sub-list.
        gap(int): The end position for the sub-list.
    Returns:
        none
    Example:
        >>> b = list_gen(100)
        >>> gap_insertion_sort(b, 5, 10)
        >>>
    """
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i
        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap

        a_list[position] = current_value


def shell_sort(a_list):
    """An algorithm that sorts a list using the shell sort method.
    Args:
        a_list(list): A list containing data to be sorted.
    Returns:
        (tuple): A tuple containing the processing time and the list, sorted.
    Example:
        >>> b = list_gen(15)
        >>> shell_sort(b)
        (0.0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    """
    strt_time = time.time()

    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)

        sublist_count = sublist_count // 2

    end_time = time.time()

    run_time = end_time - strt_time

    return (run_time, a_list)


def python_sort(a_list):
    """An algorithm that sorts a list using Python's built-in sort algorithm.
    Args:
        a_list(list): A list containing data to be sorted.
    Returns:
        (tuple): A tuple containing the processing time and the list, sorted.
    Example:
        >>> b = list_gen(10)
        >>> python_sort(b)
        (1.6927719116210938e-05, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    """
    strt_time = time.time()

    a_list.sort()

    end_time = time.time()

    run_time = end_time - strt_time

    return (run_time, a_list)


def list_gen(maxval):
    """Generates a list of random values.
    Args:
        maxval(int): An integer representing the total number of values in the
        list.
    Returns:
        samplist(list): A list of integers in random order. The list length is
        based on the maxval number entered.
    Examples:
        >>> list_gen(10)
        [6, 3, 2, 1, 4, 7, 8, 9, 5, 10]
        >>> list_gen(15)
        [7, 6, 1, 4, 8, 9, 5, 13, 12, 3, 15, 14, 2, 11, 10]
    """
    samplist = random.sample(xrange(1, (maxval + 1)), maxval)
    return samplist


def main():
    """Tests all three sort functions using 3 different sample sizes, each
    tested 100 times and returns the average processing time.
    Example:
        >>>
        For sample size 500:
        Python Sort took  0.0000091 seconds to run, on average.
        Shell Sort took  0.0006259 seconds to run, on average.
        Insertion Sort took  0.0076179 seconds to run, on average.
        For sample size 1000:
        Python Sort took  0.0000268 seconds to run, on average.
        Shell Sort took  0.0019795 seconds to run, on average.
        Insertion Sort took  0.0378560 seconds to run, on average.
        For sample size 10000:
        Python Sort took  0.0001484 seconds to run, on average.
        Shell Sort took  0.0203241 seconds to run, on average.
        Insertion Sort took  3.0973419 seconds to run, on average.
    """
    samp_size = [500, 1000, 10000]
    tests = {'Insertion': 0,
             'Shell': 0,
             'Python': 0}

    for smpl in samp_size:
        counter = 0
        while counter < 100:
            test_list = list_gen(smpl)
            tests['Insertion'] += insertion_sort(test_list)[0]
            tests['Shell'] += shell_sort(test_list)[0]
            tests['Python'] += python_sort(test_list)[0]
            counter += 1

        print 'For sample size %s:' % (smpl)

        for tst in tests:
            print ('%s Sort took %10.7f seconds to run, '
                   'on average.') % (tst, tests[tst] / counter)

if __name__ == '__main__':
    main()

