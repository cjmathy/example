import numpy as np
import random

def pointless_sort(array):
    """
    This function always returns the same values to show how testing
    works, check out the `test/test_alg.py` file to see.
    """
    return np.array([1,2,3])

def bubblesort(array):
    """
    This function sorts a numpy array using bubblesort. Bubblesort iterates over an array of length n exactly n times, and swaps the position of any misordered adjacent pairs.
    Input: array, a numpy array
    Returns: the sorted array
    """

    for n in range(np.size(array)):
        for i in range(np.size(array)-1):
            if array[i] > array[i+1]: swap(array,i,i+1)    
    return array

def quicksort(array):
    """
    This is a wrapper function which prepares a numpy array to be sorted using quicksort, called by qs
    Input: array, a numpy array
    Returns: the sorted array
    """

    p = 0
    r = array.shape[0]-1
    return qs(array,p,r)

def qs(array,first,last):
    """
    This function sorts an array with quicksort. Quicksort partitions a matrix by selecting one element (the pivot) and placing all other elements so that they are sorted correctly relative to the pivot. However, the other elements are not necessarily sorted relative to each other. Therefore, the quicksort algorithm recursively calls itself on the two subarrays below and above the excluded pivot. After all recursive calls are completed, the array is sorted.
    Inputs:
        array, a numpy array
        first, the integer index of the first element of array
        last, the integer index of the last element of array
    Returns: the sorted array
    """
    if (last > first):
        pivot = partition(array,first,last)
        qs(array,first,pivot-1)
        qs(array,pivot+1,last)
    return array

def partition(array,left,right):
    """
    This function partitions an array such that the pivot element is placed before all elements with smaller values, and after all elements with larger values.
    Inputs:
        array, a numpy array
        left, the integer index of the first element of the (sub)array to be sorted
        right, the integer index of the last element of the (sub)array to be sorted
    Returns: right, which is the integer index of the pivot's final position
    """

    pivot = left
    while(left<right):
        while (array[left] <= array[pivot] and left<right): left+=1
        while (array[right] > array[pivot]): right-=1
        if (left<right): swap(array,left,right)
    swap(array,pivot,right)
    return right

def swap(array,a,b):
    """
    This function swaps two elements in an array.
    Inputs:
        array, a numpy array
        a,b , the elements to be swapped
    Returns: Nothing
    """
    temp = array[a]
    array[a] = array[b]
    array[b] = temp
    return


