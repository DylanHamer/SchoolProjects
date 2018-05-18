"""
BubbleSort.py
Python3 implementation of Bubble Sort
by Dylan Hamer
"""

import random

"""Hybrid Bubble Sort - Mode is ascending by default"""
def hybridBubbleSort(array):
    swapped = True
    while swapped:
        swapped = False
        for index in range(len(array[:-1])):
            if array[index] > array[index+1]:
                array[index], array[index+1] = array[index+1], array[index]
                swapped = True
    return array

def bidirectionalBubbleSort(array):
    swapped = True
    correctCount = 0
    while swapped:
        swapped = False
        correctCount += 1
        for i in range(len(array[:-1])):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                swapped = True
        if not swapped: break
        swapped = False
        for index in reversed(range(len(array[:-correctCount]))):
            if array[index] > array[index+1]:
                array[index], array[index+1] = array[index+1], array[index]
                swapped = True

    return array


"""Test a sorting algorithm"""
def test(name, function, dataAmount=100):
    array = []
    for i in range(dataAmount):
        array.append(random.randint(0, 500))
    print("---{}---".format(name))
    print("Unsorted array:           {0}".format(array))
    print("Sorted array: (Ascending) {0}".format(function(array)))

test("Bidirectional Bubble Sort", bidirectionalBubbleSort, 10)
