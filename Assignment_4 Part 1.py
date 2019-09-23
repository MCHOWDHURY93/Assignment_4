#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""Assignment_4, Part 1"""

import time
import random


def sequential_search(a_list, item):
    """Searches a list for a given item and returns a boolean value as to
    whether it is present and the processing time needed to find the item.
    Args:
        a_list(list): a list containing data to be searched.
        item(various): an item or value to be searched for in the given list.
    Returns:
        (Tuple): A tuple containing the processing time in seconds, and the
        boolean value of whether the given item exists in the list.
    Examples:
        >>> i = list_gen(20)
        >>> sequential_search(i, -1)
        (1.6927719116210938e-05, False)
        >>> i = list_gen(20)
        >>> sequential_search(i, 10)
        (3.0994415283203125e-06, True)
    """
    strt_time = time.time()
    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos + 1

    end_time = time.time()

    run_time = end_time - strt_time

    return (run_time, found)


def ordered_sequential_search(a_list, item):
    """Searches an ordered list for a given item, and returns a boolean value as
    to whether it is present and the processing time needed to find the item.
    Args:
        a_list(list): a list containing data to be searched.
        item(various): an item or value to be searched for in the given list.
    Returns:
        (Tuple): A tuple containing the processing time in seconds, and the
        boolean value of whether the given item exists in the list.
    Examples:
        >>> i = list_gen(100)
        >>> ordered_sequential_search(i, -1)
        (1.6927719116210938e-05, False)
        >>> i = list_gen(100)
        >>> ordered_sequential_search(i, 50)
        (8.106231689453125e-06, True)
    """
    a_list = sorted(a_list)

    strt_time = time.time()
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
                pos = pos + 1

    end_time = time.time()

    run_time = end_time - strt_time

    return (run_time, found)


def binary_search_iterative(a_list, item):
    """Searches an ordered list for a given item, and returns a boolean value as
    to whether it is present and the processing time needed to find the item.
    Args:
        a_list(list): a list containing data to be searched.
        item(various): an item or value to be searched for in the given list.
    Returns:
        (Tuple): A tuple containing the processing time in seconds, and the
        boolean value of whether the given item exists in the list.
    Examples:
        >>> i = list_gen(1000)
        >>> binary_search_iterative(i, -10)
        (4.0531158447265625e-06, False)
        >>> i = list_gen(1000)
        >>> binary_search_iterative(i, 595)
        (8.082389831542969e-05, True)
    """
    a_list = sorted(a_list)

    strt_time = time.time()
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

    end_time = time.time()

    run_time = end_time - strt_time

    return (run_time, found)


def binary_search_recursive(a_list, item):
    """Searches an ordered list for a given item, and returns a boolean value as
    to whether it is present and the processing time needed to find the item.
    Args:
        a_list(list): a list containing data to be searched.
        item(various): an item or value to be searched for in the given list.
    Returns:
        (Tuple): A tuple containing the processing time in seconds, and the
        boolean value of whether the given item exists in the list.
    Examples:
        >>> i = list_gen(211)
        >>> binary_search_recursive(i, -1)
        (1.0967254638671875e-05, False)
        >>> i = list_gen(211)
        >>> binary_search_recursive(i, 200)
        (4.0531158447265625e-06, True)"""
    a_list = sorted(a_list)

    strt_time = time.time()

    if len(a_list) == 0:
        found = False
    else:
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                return binary_search_recursive(a_list[:midpoint], item)
            else:
                return binary_search_recursive(a_list[midpoint + 1:], item)

    end_time = time.time()

    run_time = end_time - strt_time

    return (run_time, found)


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
    """Tests the 4 different search algorithms by generating 100 test lists of
    three different sizes, then calculates the average processing time for each
    and returns the results in string.
    Args:
        None.
    Returns:
        (String): Processing time averages for each test.
    Example:
        For sample size 500:
        Bin Iterative Search took  0.0000029 seconds to run, on average.
        Sequential Search took  0.0000561 seconds to run, on average.
        Ordered Search took  0.0000015 seconds to run, on average.
        Bin Recursive Search took  0.0000005 seconds to run, on average.
        For sample size 1000:
        Bin Iterative Search took  0.0000061 seconds to run, on average.
        Sequential Search took  0.0001835 seconds to run, on average.
        Ordered Search took  0.0000030 seconds to run, on average.
        Bin Recursive Search took  0.0000010 seconds to run, on average.
        For sample size 10000:
        Bin Iterative Search took  0.0000215 seconds to run, on average.
        Sequential Search took  0.0013535 seconds to run, on average.
        Ordered Search took  0.0000123 seconds to run, on average.
        Bin Recursive Search took  0.0000028 seconds to run, on average.
    """

    samp_size = [500, 1000, 10000]
    tests = {'Sequential': 0,
             'Ordered': 0,
             'Bin Iterative': 0,
             'Bin Recursive': 0}

    for smpl in samp_size:
        counter = 0
        while counter < 100:
            test_list = list_gen(smpl)
            tests['Sequential'] += sequential_search(test_list, -1)[0]
            tests['Ordered'] += ordered_sequential_search(test_list, -1)[0]
            tests['Bin Iterative'] += binary_search_iterative(test_list, -1)[0]
            tests['Bin Recursive'] += binary_search_recursive(test_list, -1)[0]
            counter += 1

        print 'For sample size %s:' % (smpl)

        for tst in tests:
            print ('%s Search took %10.7f seconds to run, '
                   'on average.') % (tst, tests[tst] / counter)


if __name__ == "__main__":
    main()

